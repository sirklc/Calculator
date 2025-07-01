# 🧮 Hesap Makinesi Pro

Modern, kullanıcı dostu Python hesap makinesi uygulaması. Temel matematik işlemlerinden ileri bilimsel hesaplamalara kadar geniş özellik yelpazesi sunar.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20|%20macOS%20|%20Linux-lightgrey.svg)

## ✨ Özellikler

### 🔢 Temel İşlemler
- ➕ Toplama, çıkarma, çarpma, bölme
- 🔢 Ondalık sayı desteği
- ➕➖ İşaret değiştirme
- ⌫ Geri silme ve temizleme

### 🔬 Bilimsel İşlemler
- √ Karekök hesaplama
- x² Kare alma
- x^y Üs alma
- 📐 Trigonometrik fonksiyonlar (sin, cos, tan)
- 📊 Logaritma işlemleri (log, ln)
- ! Faktöriyel hesaplama

### 🧠 Akıllı Özellikler
- 💾 Hafıza işlemleri (MC, MR, M+, M-)
- 📜 Hesaplama geçmişi
- ⌨️ Tam klavye desteği
- 🎯 Hata yönetimi ve kullanıcı dostu mesajlar

## 🚀 Hızlı Başlangıç

### 📋 Gereksinimler
- Python 3.6 veya üzeri
- tkinter (Python ile birlikte gelir)

### ⚡ Kurulum ve Çalıştırma

```bash
# Projeyi klonlayın
git clone https://github.com/sirklc/Calculator.git
cd Calculator

# Hesap makinesini çalıştırın
python3 main.py
```

**Bu kadar! 🎉 Hesap makinesi otomatik olarak açılacak.**

## 📁 Proje Yapısı

```
Calculator/
├── main.py              # 🚀 Ana başlatıcı
├── src/                 # 📦 Kaynak kodlar
│   ├── calculator.py    # 🔧 Hesap makinesi motoru
│   └── calculator_gui.py # 🖥️ Grafik arayüz
├── tests/               # 🧪 Test dosyaları
│   ├── test_calculator.py
│   ├── test_calculator_class.py
│   └── run_tests.py     # Test çalıştırıcı
├── docs/                # 📚 Dokümantasyon
├── README.md            # 📖 Bu dosya
└── LICENSE              # 📜 MIT Lisansı
```

## 🎮 Kullanım

### 🖱️ Fare ile Kullanım
- Sayıları ve işlemleri butonlara tıklayarak girin
- Hafıza butonlarını kullanarak değerleri saklayın
- "Geçmiş" butonuyla hesaplama geçmişini görüntüleyin

### ⌨️ Klavye Kısayolları

| Tuş | İşlev |
|-----|-------|
| `0-9` | Sayı girişi |
| `+` `-` `*` `/` | Matematik işlemleri |
| `=` `Enter` | Sonuç hesaplama |
| `Backspace` | Son karakteri sil |
| `Delete` `C` | Hepsini temizle |
| `Escape` | Girişi temizle |

### 📖 Örnek Kullanım

```
Basit hesaplama:
5 + 3 = 8

Bilimsel hesaplama:
√25 = 5
2^8 = 256
sin(30°) = 0.5

Hafıza kullanımı:
1. Sayıyı girin: 100
2. "M+" butonuna basın
3. Başka hesaplamalar yapın
4. "MR" ile hafızadaki değeri çağırın
```

## 🧪 Test Etme

```bash
# Tüm testleri çalıştır
cd tests
python3 run_tests.py

# Tek test dosyası çalıştır
python3 test_calculator.py
```

## 🎯 Özellik Detayları

### Hafıza İşlemleri
- **MC**: Hafızayı temizle
- **MR**: Hafızadaki değeri çağır
- **M+**: Mevcut değeri hafızaya ekle
- **M-**: Mevcut değeri hafızadan çıkar

### Bilimsel Fonksiyonlar
- **Trigonometrik**: Açılar derece cinsinden işlenir
- **Logaritma**: 10 tabanında ve doğal logaritma
- **Faktöriyel**: Tam sayılar için n! hesaplama
- **Kökler**: Karekök ve üs ile genel kök hesaplama

### Hata Yönetimi
- ✅ Sıfıra bölme koruması
- ✅ Negatif sayının karekökü koruması  
- ✅ Geçersiz giriş koruması
- ✅ Açık ve anlaşılır hata mesajları

## 🔧 Geliştirici Bilgileri

### Kod Yapısı
```python
# Calculator sınıfı kullanımı
from src.calculator import Calculator

calc = Calculator()
result = calc.add(5, 3)        # Toplama
calc.memory_store(result)      # Hafızaya kaydet
history = calc.get_history()   # Geçmişi al
```

### Yeni Özellik Ekleme
1. `src/calculator.py` dosyasına yeni fonksiyon ekleyin
2. `src/calculator_gui.py` dosyasına buton ekleyin
3. `tests/` klasörüne test yazın
4. Test edin ve belgelendirin

## 🐛 Bilinen Sorunlar

- Çok büyük sayılarla taşma (overflow) olabilir
- Kompleks sayı desteği sınırlı

## 🤝 Katkıda Bulunma

1. 🍴 Projeyi fork edin
2. 🌟 Yeni özellik dalı oluşturun
3. 💻 Değişikliklerinizi yapın
4. 🧪 Testlerinizi yazın
5. 📝 Pull request gönderin

## 📝 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 📧 İletişim

- **E-posta**: [info@sirklc.com.tr](mailto:info@sirklc.com.tr)
- **GitHub**: [@sirklc](https://github.com/sirklc)

## 🌟 Teşekkürler

Bu projeyi incelediğiniz için teşekkürler! Beğendiyseniz ⭐ vermeyi unutmayın.

---

**Versiyon**: 2.1  
**Son Güncelleme**: 2024  
**Platform Desteği**: Windows, macOS, Linux