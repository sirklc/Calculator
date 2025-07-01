import unittest
import math
import sys
import os

# Src klasörünü Python yoluna ekle
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from calculator import Calculator


class TestCalculatorClass(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_basic_operations(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.divide(6, 2), 3)
        
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    def test_power_and_roots(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.square_root(4), 2.0)
        self.assertAlmostEqual(self.calc.root(8, 3), 2)
        
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)
    
    def test_trigonometric_functions(self):
        self.assertAlmostEqual(self.calc.sine(0), 0)
        self.assertAlmostEqual(self.calc.cosine(0), 1)
        self.assertAlmostEqual(self.calc.tangent(0), 0)
    
    def test_logarithmic_functions(self):
        self.assertAlmostEqual(self.calc.logarithm(100, 10), 2)
        self.assertAlmostEqual(self.calc.natural_log(math.e), 1)
        
        with self.assertRaises(ValueError):
            self.calc.logarithm(0, 10)
    
    def test_combinatorial_functions(self):
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.combination(5, 2), 10)
        self.assertEqual(self.calc.permutation(5, 2), 20)
        
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)
    
    def test_conversion_functions(self):
        self.assertAlmostEqual(self.calc.degrees_to_radians(180), math.pi)
        self.assertAlmostEqual(self.calc.radians_to_degrees(math.pi), 180)
    
    def test_utility_functions(self):
        self.assertEqual(self.calc.absolute_value(-5), 5)
        self.assertEqual(self.calc.percent(100, 50), 50)
    
    def test_memory_operations(self):
        self.calc.memory_store(10)
        self.assertEqual(self.calc.memory_recall(), 10)
        
        self.calc.memory_add(5)
        self.assertEqual(self.calc.memory_recall(), 15)
        
        self.calc.memory_subtract(3)
        self.assertEqual(self.calc.memory_recall(), 12)
        
        self.calc.memory_clear()
        self.assertEqual(self.calc.memory_recall(), 0)
    
    def test_history_operations(self):
        self.calc.add(2, 3)
        self.calc.multiply(4, 5)
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)
        self.assertIn("2 + 3 = 5", history)
        self.assertIn("4 × 5 = 20", history)
        
        self.assertEqual(self.calc.get_last_result(), 20)
        
        self.calc.clear_history()
        self.assertEqual(len(self.calc.get_history()), 0)
    
    def test_complex_operations(self):
        z1 = complex(1, 2)
        z2 = complex(3, 4)
        
        result = self.calc.add_complex(z1, z2)
        self.assertEqual(result, complex(4, 6))
        
        result = self.calc.multiply_complex(z1, z2)
        self.assertEqual(result, complex(-5, 10))
        
        magnitude = self.calc.complex_magnitude(complex(3, 4))
        self.assertEqual(magnitude, 5)
        
        phase = self.calc.complex_phase(complex(1, 1))
        self.assertAlmostEqual(phase, math.pi/4)
    
    def test_scientific_notation(self):
        sci_notation = self.calc.to_scientific_notation(1234.5, 2)
        self.assertEqual(sci_notation, "1.23e+03")
        
        number = self.calc.from_scientific_notation("1.23e+03")
        self.assertEqual(number, 1230.0)


if __name__ == '__main__':
    unittest.main()