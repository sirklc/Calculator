#!/usr/bin/env python3
"""
Hesap Makinesi Pro - Ana Başlatıcı
Bu dosyayı çalıştırarak hesap makinesini başlatabilirsiniz.
"""

import sys
import os

def main():
    """Ana başlatma fonksiyonu"""
    print("🧮 Hesap Makinesi Pro başlatılıyor...")
    
    # src klasörünü Python yoluna ekle
    src_path = os.path.join(os.path.dirname(__file__), 'src')
    sys.path.insert(0, src_path)
    
    try:
        from calculator_gui import main as gui_main
        gui_main()
    except ImportError as e:
        print(f"❌ Hata: Gerekli modüller bulunamadı - {e}")
        print("Lütfen tüm dosyaların yerinde olduğundan emin olun.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Beklenmeyen hata: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()