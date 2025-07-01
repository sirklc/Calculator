import math
from math import factorial as math_factorial


class Calculator:
    def __init__(self):
        self.memory = 0
        self.history = []
        self.last_result = 0
    
    # Basic arithmetic operations
    def add(self, x, y):
        """Adds two numbers."""
        result = x + y
        self._add_to_history(f"{x} + {y}", result)
        return result

    def subtract(self, x, y):
        """Subtracts second number from the first."""
        result = x - y
        self._add_to_history(f"{x} - {y}", result)
        return result

    def multiply(self, x, y):
        """Multiplies two numbers."""
        result = x * y
        self._add_to_history(f"{x} × {y}", result)
        return result

    def divide(self, x, y):
        """Divides first number by the second. Raises an error if the second number is zero."""
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        result = x / y
        self._add_to_history(f"{x} ÷ {y}", result)
        return result

    def power(self, x, y):
        """Raises x to the power of y."""
        result = x ** y
        self._add_to_history(f"{x}^{y}", result)
        return result

    # Advanced mathematical operations
    def square_root(self, x):
        """Returns the square root of x."""
        if x < 0:
            raise ValueError("Cannot take the square root of a negative number!")
        result = math.sqrt(x)
        self._add_to_history(f"√{x}", result)
        return result

    def root(self, x, n):
        """Returns the nth root of x."""
        if n == 0:
            raise ValueError("Cannot take the 0th root!")
        if x < 0 and n % 2 == 0:
            raise ValueError("Cannot take even root of negative number!")
        result = x ** (1/n)
        self._add_to_history(f"{n}√{x}", result)
        return result

    def absolute_value(self, x):
        """Returns the absolute value of x."""
        result = abs(x)
        self._add_to_history(f"|{x}|", result)
        return result

    # Trigonometric functions
    def sine(self, x):
        """Returns the sine of x (x in radians)."""
        result = math.sin(x)
        self._add_to_history(f"sin({x})", result)
        return result

    def cosine(self, x):
        """Returns the cosine of x (x in radians)."""
        result = math.cos(x)
        self._add_to_history(f"cos({x})", result)
        return result

    def tangent(self, x):
        """Returns the tangent of x (x in radians)."""
        result = math.tan(x)
        self._add_to_history(f"tan({x})", result)
        return result

    # Logarithmic functions
    def logarithm(self, x, base=10):
        """Returns the logarithm of x with the given base."""
        if x <= 0:
            raise ValueError("Logarithm only defined for positive numbers!")
        result = math.log(x, base)
        self._add_to_history(f"log₍{base}₎({x})", result)
        return result

    def natural_log(self, x):
        """Returns the natural logarithm of x."""
        if x <= 0:
            raise ValueError("Natural logarithm only defined for positive numbers!")
        result = math.log(x)
        self._add_to_history(f"ln({x})", result)
        return result

    # Combinatorial functions
    def factorial(self, n):
        """Returns the factorial of n."""
        if n < 0:
            raise ValueError("Factorial only defined for non-negative integers!")
        if not isinstance(n, int):
            raise ValueError("Factorial only defined for integers!")
        result = math_factorial(n)
        self._add_to_history(f"{n}!", result)
        return result

    def combination(self, n, r):
        """Returns the number of combinations of n items taken r at a time."""
        if n < 0 or r < 0:
            raise ValueError("Combination only defined for non-negative integers!")
        if not isinstance(n, int) or not isinstance(r, int):
            raise ValueError("Combination only defined for integers!")
        if r > n:
            result = 0
        else:
            result = math_factorial(n) // (math_factorial(r) * math_factorial(n - r))
        self._add_to_history(f"C({n},{r})", result)
        return result

    def permutation(self, n, r):
        """Returns the number of permutations of n items taken r at a time."""
        if n < 0 or r < 0:
            raise ValueError("Permutation only defined for non-negative integers!")
        if not isinstance(n, int) or not isinstance(r, int):
            raise ValueError("Permutation only defined for integers!")
        if r > n:
            result = 0
        else:
            result = math_factorial(n) // math_factorial(n - r)
        self._add_to_history(f"P({n},{r})", result)
        return result

    # Conversion functions
    def degrees_to_radians(self, degrees):
        """Converts degrees to radians."""
        result = math.radians(degrees)
        self._add_to_history(f"{degrees}° → rad", result)
        return result

    def radians_to_degrees(self, radians):
        """Converts radians to degrees."""
        result = math.degrees(radians)
        self._add_to_history(f"{radians} rad → °", result)
        return result

    # Utility functions
    def percent(self, x, percentage):
        """Returns the percentage of x."""
        result = x * (percentage / 100)
        self._add_to_history(f"{percentage}% of {x}", result)
        return result

    # Memory operations
    def memory_store(self, value):
        """Store value in memory."""
        self.memory = value
        return self.memory

    def memory_recall(self):
        """Recall value from memory."""
        return self.memory

    def memory_clear(self):
        """Clear memory."""
        self.memory = 0
        return self.memory

    def memory_add(self, value):
        """Add value to memory."""
        self.memory += value
        return self.memory

    def memory_subtract(self, value):
        """Subtract value from memory."""
        self.memory -= value
        return self.memory

    # History operations
    def _add_to_history(self, operation, result):
        """Add calculation to history."""
        self.history.append(f"{operation} = {result}")
        self.last_result = result
        if len(self.history) > 100:  # Keep only last 100 operations
            self.history.pop(0)

    def get_history(self):
        """Get calculation history."""
        return self.history.copy()

    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()

    def get_last_result(self):
        """Get the last calculation result."""
        return self.last_result

    # Complex number operations
    def add_complex(self, z1, z2):
        """Add two complex numbers."""
        if not isinstance(z1, complex):
            z1 = complex(z1)
        if not isinstance(z2, complex):
            z2 = complex(z2)
        result = z1 + z2
        self._add_to_history(f"{z1} + {z2}", result)
        return result

    def multiply_complex(self, z1, z2):
        """Multiply two complex numbers."""
        if not isinstance(z1, complex):
            z1 = complex(z1)
        if not isinstance(z2, complex):
            z2 = complex(z2)
        result = z1 * z2
        self._add_to_history(f"{z1} × {z2}", result)
        return result

    def complex_magnitude(self, z):
        """Return the magnitude of a complex number."""
        if not isinstance(z, complex):
            z = complex(z)
        result = abs(z)
        self._add_to_history(f"|{z}|", result)
        return result

    def complex_phase(self, z):
        """Return the phase of a complex number in radians."""
        if not isinstance(z, complex):
            z = complex(z)
        result = math.atan2(z.imag, z.real)
        self._add_to_history(f"arg({z})", result)
        return result

    # Scientific notation support
    def to_scientific_notation(self, number, precision=2):
        """Convert number to scientific notation."""
        return f"{number:.{precision}e}"

    def from_scientific_notation(self, sci_string):
        """Convert scientific notation string to float."""
        return float(sci_string)