#!/usr/bin/env python3
"""
Hesap Makinesi - Ana Arayüz
Modern ve kullanıcı dostu grafik arayüz
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math
import sys
import os

# Calculator class'ını import et
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from src.calculator import Calculator
except ImportError:
    from calculator import Calculator


class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hesap Makinesi Pro")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        
        # Pencereyi ekranın ortasına yerleştir
        self.center_window()
        
        # Hesap makinesi nesnesi
        self.calc = Calculator()
        
        # Mevcut durum
        self.current_input = ""
        self.operation_pending = False
        self.pending_operation = None
        self.pending_value = None
        
        # Arayüzü oluştur
        self.create_widgets()
        
        # Klavye bağlamaları
        self.setup_keyboard_bindings()
        
    def center_window(self):
        """Pencereyi ekranın ortasına yerleştir"""
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        window_width = 400
        window_height = 550
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
    def create_widgets(self):
        """Arayüz elemanlarını oluştur"""
        # Ana çerçeve
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Ekran çerçevesi
        display_frame = ttk.LabelFrame(main_frame, text="", padding="10")
        display_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Ana ekran
        self.display_var = tk.StringVar(value="0")
        display_label = tk.Label(display_frame, 
                               textvariable=self.display_var,
                               font=('Arial', 20, 'bold'),
                               bg='white', fg='black',
                               relief='sunken',
                               anchor='e',
                               width=20, height=2)
        display_label.pack(fill=tk.X)
        
        # Hafıza butonları
        memory_frame = ttk.LabelFrame(main_frame, text="Hafıza", padding="5")
        memory_frame.pack(fill=tk.X, pady=(0, 10))
        
        memory_buttons = [
            ("MC", self.memory_clear),
            ("MR", self.memory_recall),
            ("M+", self.memory_add),
            ("M-", self.memory_subtract),
            ("Geçmiş", self.show_history)
        ]
        
        for i, (text, command) in enumerate(memory_buttons):
            btn = ttk.Button(memory_frame, text=text, command=command, width=7)
            btn.grid(row=0, column=i, padx=2)
        
        # Ana buton çerçevesi
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill=tk.BOTH, expand=True)
        
        # Buton boyutları
        btn_width = 8
        btn_height = 2
        
        # İlk satır: Temizleme ve işlem butonları
        ttk.Button(buttons_frame, text="C", command=self.clear_all, width=btn_width).grid(row=0, column=0, padx=2, pady=2, sticky='nsew')
        ttk.Button(buttons_frame, text="CE", command=self.clear_entry, width=btn_width).grid(row=0, column=1, padx=2, pady=2, sticky='nsew')
        ttk.Button(buttons_frame, text="⌫", command=self.backspace, width=btn_width).grid(row=0, column=2, padx=2, pady=2, sticky='nsew')
        ttk.Button(buttons_frame, text="÷", command=lambda: self.handle_operation('divide'), width=btn_width).grid(row=0, column=3, padx=2, pady=2, sticky='nsew')
        
        # Sayı ve işlem butonları
        buttons = [
            # Satır 1
            [('7', lambda: self.input_number('7')), ('8', lambda: self.input_number('8')), ('9', lambda: self.input_number('9')), ('×', lambda: self.handle_operation('multiply'))],
            # Satır 2
            [('4', lambda: self.input_number('4')), ('5', lambda: self.input_number('5')), ('6', lambda: self.input_number('6')), ('-', lambda: self.handle_operation('subtract'))],
            # Satır 3
            [('1', lambda: self.input_number('1')), ('2', lambda: self.input_number('2')), ('3', lambda: self.input_number('3')), ('+', lambda: self.handle_operation('add'))],
            # Satır 4
            [('±', self.change_sign), ('0', lambda: self.input_number('0')), ('.', lambda: self.input_number('.')), ('=', lambda: self.handle_operation('equals'))]
        ]
        
        for row_idx, row in enumerate(buttons, 1):
            for col_idx, (text, command) in enumerate(row):
                btn = ttk.Button(buttons_frame, text=text, command=command, width=btn_width)
                btn.grid(row=row_idx, column=col_idx, padx=2, pady=2, sticky='nsew')
        
        # Bilimsel işlemler
        scientific_frame = ttk.LabelFrame(main_frame, text="Bilimsel İşlemler", padding="5")
        scientific_frame.pack(fill=tk.X, pady=(10, 0))
        
        sci_buttons = [
            [('√', self.sqrt_operation), ('x²', self.square_operation), ('x^y', lambda: self.handle_operation('power'))],
            [('sin', self.sin_operation), ('cos', self.cos_operation), ('tan', self.tan_operation)],
            [('log', self.log_operation), ('ln', self.ln_operation), ('n!', self.factorial_operation)]
        ]
        
        for row_idx, row in enumerate(sci_buttons):
            for col_idx, (text, command) in enumerate(row):
                btn = ttk.Button(scientific_frame, text=text, command=command, width=8)
                btn.grid(row=row_idx, column=col_idx, padx=2, pady=2)
        
        # Grid ağırlıklarını ayarla
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
            
    def setup_keyboard_bindings(self):
        """Klavye kısayollarını ayarla"""
        self.root.bind('<Key>', self.handle_keypress)
        self.root.focus_set()
        
    def handle_keypress(self, event):
        """Klavye girişlerini işle"""
        key = event.char
        
        if key.isdigit() or key == '.':
            self.input_number(key)
        elif key == '+':
            self.handle_operation('add')
        elif key == '-':
            self.handle_operation('subtract')
        elif key == '*':
            self.handle_operation('multiply')
        elif key == '/':
            self.handle_operation('divide')
        elif key == '=' or event.keysym == 'Return':
            self.handle_operation('equals')
        elif event.keysym == 'BackSpace':
            self.backspace()
        elif event.keysym == 'Delete' or key.lower() == 'c':
            self.clear_all()
        elif event.keysym == 'Escape':
            self.clear_entry()
            
    def input_number(self, number):
        """Sayı girişi"""
        if self.display_var.get() == "0" or self.operation_pending:
            self.display_var.set(number)
            self.operation_pending = False
        else:
            if number == '.' and '.' in self.display_var.get():
                return
            current = self.display_var.get()
            self.display_var.set(current + number)
        
    def handle_operation(self, operation):
        """İşlem işleme"""
        try:
            current_value = float(self.display_var.get())
            
            if operation == 'equals':
                if self.pending_operation and self.pending_value is not None:
                    if self.pending_operation == 'add':
                        result = self.calc.add(self.pending_value, current_value)
                    elif self.pending_operation == 'subtract':
                        result = self.calc.subtract(self.pending_value, current_value)
                    elif self.pending_operation == 'multiply':
                        result = self.calc.multiply(self.pending_value, current_value)
                    elif self.pending_operation == 'divide':
                        result = self.calc.divide(self.pending_value, current_value)
                    elif self.pending_operation == 'power':
                        result = self.calc.power(self.pending_value, current_value)
                    
                    self.display_var.set(str(result))
                    self.pending_operation = None
                    self.pending_value = None
            else:
                self.pending_operation = operation
                self.pending_value = current_value
                self.operation_pending = True
                
        except Exception as e:
            messagebox.showerror("Hata", str(e))
            self.clear_all()
            
    # Bilimsel işlemler
    def sqrt_operation(self):
        """Karekök işlemi"""
        try:
            value = float(self.display_var.get())
            result = self.calc.square_root(value)
            self.display_var.set(str(result))
        except Exception as e:
            messagebox.showerror("Hata", str(e))
            
    def square_operation(self):
        """Kare işlemi"""
        try:
            value = float(self.display_var.get())
            result = self.calc.power(value, 2)
            self.display_var.set(str(result))
        except Exception as e:
            messagebox.showerror("Hata", str(e))
            
    def sin_operation(self):
        """Sinüs işlemi"""
        try:
            value = float(self.display_var.get())
            result = self.calc.sine(math.radians(value))  # Derece cinsinden
            self.display_var.set(str(result))
        except Exception as e:
            messagebox.showerror("Hata", str(e))
            
    def cos_operation(self):
        """Kosinüs işlemi"""
        try:
            value = float(self.display_var.get())
            result = self.calc.cosine(math.radians(value))  # Derece cinsinden
            self.display_var.set(str(result))
        except Exception as e:
            messagebox.showerror("Hata", str(e))
            
    def tan_operation(self):
        """Tanjant işlemi"""
        try:
            value = float(self.display_var.get())
            result = self.calc.tangent(math.radians(value))  # Derece cinsinden
            self.display_var.set(str(result))
        except Exception as e:
            messagebox.showerror("Hata", str(e))
            
    def log_operation(self):
        """Logaritma işlemi"""
        try:
            value = float(self.display_var.get())
            result = self.calc.logarithm(value, 10)
            self.display_var.set(str(result))
        except Exception as e:
            messagebox.showerror("Hata", str(e))
            
    def ln_operation(self):
        """Doğal logaritma işlemi"""
        try:
            value = float(self.display_var.get())
            result = self.calc.natural_log(value)
            self.display_var.set(str(result))
        except Exception as e:
            messagebox.showerror("Hata", str(e))
            
    def factorial_operation(self):
        """Faktöriyel işlemi"""
        try:
            value = int(float(self.display_var.get()))
            result = self.calc.factorial(value)
            self.display_var.set(str(result))
        except Exception as e:
            messagebox.showerror("Hata", str(e))
    
    # Temel işlemler
    def clear_all(self):
        """Hepsini temizle"""
        self.display_var.set("0")
        self.pending_operation = None
        self.pending_value = None
        self.operation_pending = False
        
    def clear_entry(self):
        """Girişi temizle"""
        self.display_var.set("0")
        
    def backspace(self):
        """Geri silme"""
        current = self.display_var.get()
        if len(current) > 1:
            self.display_var.set(current[:-1])
        else:
            self.display_var.set("0")
        
    def change_sign(self):
        """İşaret değiştir"""
        current = self.display_var.get()
        if current != "0":
            if current.startswith('-'):
                self.display_var.set(current[1:])
            else:
                self.display_var.set('-' + current)
            
    # Hafıza işlemleri
    def memory_clear(self):
        """Hafızayı temizle"""
        self.calc.memory_clear()
        messagebox.showinfo("Bilgi", "Hafıza temizlendi")
        
    def memory_recall(self):
        """Hafızayı çağır"""
        value = self.calc.memory_recall()
        self.display_var.set(str(value))
        
    def memory_add(self):
        """Hafızaya ekle"""
        try:
            value = float(self.display_var.get())
            self.calc.memory_add(value)
            messagebox.showinfo("Bilgi", f"Hafızaya {value} eklendi")
        except ValueError:
            messagebox.showerror("Hata", "Geçersiz sayı")
        
    def memory_subtract(self):
        """Hafızadan çıkar"""
        try:
            value = float(self.display_var.get())
            self.calc.memory_subtract(value)
            messagebox.showinfo("Bilgi", f"Hafızadan {value} çıkarıldı")
        except ValueError:
            messagebox.showerror("Hata", "Geçersiz sayı")
        
    def show_history(self):
        """Geçmişi göster"""
        history_window = tk.Toplevel(self.root)
        history_window.title("Hesaplama Geçmişi")
        history_window.geometry("350x400")
        history_window.transient(self.root)
        
        # Pencereyi ana pencerenin yanına yerleştir
        x = self.root.winfo_x() + self.root.winfo_width() + 10
        y = self.root.winfo_y()
        history_window.geometry(f"350x400+{x}+{y}")
        
        frame = ttk.Frame(history_window, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Metin kutusu
        text_widget = tk.Text(frame, wrap=tk.WORD, width=40, height=20)
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)
        
        # Geçmişi ekle
        history = self.calc.get_history()
        if history:
            for i, item in enumerate(history, 1):
                text_widget.insert(tk.END, f"{i}. {item}\n")
        else:
            text_widget.insert(tk.END, "Henüz hesaplama yapılmadı.")
            
        text_widget.config(state=tk.DISABLED)
        
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Temizle butonu
        ttk.Button(history_window, text="Geçmişi Temizle", 
                  command=lambda: [self.calc.clear_history(), history_window.destroy()]).pack(pady=10)


def main():
    """Ana program"""
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()