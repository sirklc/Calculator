import unittest
import math
import sys
import os

# Src klasörünü Python yoluna ekle
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from calculator import Calculator

# Test için calculator instance oluştur
calc = Calculator()

# Fonksiyonları calculator instance'ından al
add = calc.add
subtract = calc.subtract
multiply = calc.multiply
divide = calc.divide
power = calc.power
square_root = calc.square_root
absolute_value = calc.absolute_value
sine = calc.sine
cosine = calc.cosine
tangent = calc.tangent
logarithm = calc.logarithm
natural_log = calc.natural_log
factorial = calc.factorial
combination = calc.combination
permutation = calc.permutation
degrees_to_radians = calc.degrees_to_radians
radians_to_degrees = calc.radians_to_degrees
root = calc.root
percent = calc.percent


class TestCalculatorFunctions(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(2.5, 3.7), 6.2)
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -2), -1)
        self.assertEqual(subtract(7.5, 2.5), 5.0)
    
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(2.5, 4), 10.0)
    
    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(-6, 2), -3)
        self.assertEqual(divide(7.5, 2.5), 3.0)
        
        with self.assertRaises(ValueError):
            divide(5, 0)
    
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, -1), 0.5)
        self.assertEqual(power(4, 0.5), 2.0)
    
    def test_square_root(self):
        self.assertEqual(square_root(4), 2.0)
        self.assertEqual(square_root(0), 0.0)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))
        
        with self.assertRaises(ValueError):
            square_root(-1)
    
    def test_absolute_value(self):
        self.assertEqual(absolute_value(5), 5)
        self.assertEqual(absolute_value(-5), 5)
        self.assertEqual(absolute_value(0), 0)
        self.assertEqual(absolute_value(-3.7), 3.7)
    
    def test_sine(self):
        self.assertAlmostEqual(sine(0), 0)
        self.assertAlmostEqual(sine(math.pi/2), 1)
        self.assertAlmostEqual(sine(math.pi), 0, places=10)
        self.assertAlmostEqual(sine(math.pi/6), 0.5)
    
    def test_cosine(self):
        self.assertAlmostEqual(cosine(0), 1)
        self.assertAlmostEqual(cosine(math.pi/2), 0, places=10)
        self.assertAlmostEqual(cosine(math.pi), -1)
        self.assertAlmostEqual(cosine(math.pi/3), 0.5)
    
    def test_tangent(self):
        self.assertAlmostEqual(tangent(0), 0)
        self.assertAlmostEqual(tangent(math.pi/4), 1)
        self.assertAlmostEqual(tangent(math.pi), 0, places=10)
    
    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(100, 10), 2)
        self.assertAlmostEqual(logarithm(8, 2), 3)
        self.assertAlmostEqual(logarithm(1, 10), 0)
        
        with self.assertRaises(ValueError):
            logarithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(-1, 10)
    
    def test_natural_log(self):
        self.assertAlmostEqual(natural_log(math.e), 1)
        self.assertAlmostEqual(natural_log(1), 0)
        self.assertAlmostEqual(natural_log(math.e**2), 2)
        
        with self.assertRaises(ValueError):
            natural_log(0)
        with self.assertRaises(ValueError):
            natural_log(-1)
    
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(3.5)
    
    def test_combination(self):
        self.assertEqual(combination(5, 2), 10)
        self.assertEqual(combination(4, 0), 1)
        self.assertEqual(combination(6, 6), 1)
        self.assertEqual(combination(3, 5), 0)
        
        with self.assertRaises(ValueError):
            combination(-1, 2)
        with self.assertRaises(ValueError):
            combination(5.5, 2)
    
    def test_permutation(self):
        self.assertEqual(permutation(5, 2), 20)
        self.assertEqual(permutation(4, 0), 1)
        self.assertEqual(permutation(6, 6), 720)
        self.assertEqual(permutation(3, 5), 0)
        
        with self.assertRaises(ValueError):
            permutation(-1, 2)
        with self.assertRaises(ValueError):
            permutation(5.5, 2)
    
    def test_degrees_to_radians(self):
        self.assertAlmostEqual(degrees_to_radians(180), math.pi)
        self.assertAlmostEqual(degrees_to_radians(90), math.pi/2)
        self.assertAlmostEqual(degrees_to_radians(0), 0)
    
    def test_radians_to_degrees(self):
        self.assertAlmostEqual(radians_to_degrees(math.pi), 180)
        self.assertAlmostEqual(radians_to_degrees(math.pi/2), 90)
        self.assertAlmostEqual(radians_to_degrees(0), 0)
    
    def test_root(self):
        self.assertAlmostEqual(root(8, 3), 2)
        self.assertAlmostEqual(root(16, 4), 2)
        self.assertAlmostEqual(root(1, 5), 1)
        
        with self.assertRaises(ValueError):
            root(4, 0)
        with self.assertRaises(ValueError):
            root(-4, 2)
    
    def test_percent(self):
        self.assertAlmostEqual(percent(100, 50), 50)
        self.assertAlmostEqual(percent(200, 25), 50)
        self.assertAlmostEqual(percent(80, 10), 8)


if __name__ == '__main__':
    unittest.main()