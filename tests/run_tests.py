#!/usr/bin/env python3
"""
Test Runner - Tüm testleri çalıştır
"""

import sys
import os
import unittest

# Ana dizin ve src klasörünü Python yoluna ekle
project_root = os.path.dirname(os.path.dirname(__file__))
src_path = os.path.join(project_root, 'src')
sys.path.insert(0, project_root)
sys.path.insert(0, src_path)

def run_all_tests():
    """Tüm testleri çalıştır"""
    print("🧪 Test süiti başlatılıyor...")
    print("=" * 40)
    
    # Test dosyalarını bul ve çalıştır
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('.', pattern='test_*.py')
    
    # Test çalıştırıcısı
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Sonuçları raporla
    print("\n" + "=" * 40)
    if result.wasSuccessful():
        print("✅ Tüm testler başarılı!")
    else:
        print(f"❌ {len(result.failures)} test başarısız, {len(result.errors)} hata")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)