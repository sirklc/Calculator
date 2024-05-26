import math

def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts second number from the first."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides first number by the second. Raises an error if the second number is zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def power(x, y):
    """Raises x to the power of y."""
    return x ** y

def square_root(x):
    """Returns the square root of x."""
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number!")
    return math.sqrt(x)

def absolute_value(x):
    """Returns the absolute value of x."""
    return abs(x)

def sine(x):
    """Returns the sine of x (x in radians)."""
    return math.sin(x)

def cosine(x):
    """Returns the cosine of x (x in radians)."""
    return math.cos(x)

def tangent(x):
    """Returns the tangent of x (x in radians)."""
    return math.tan(x)

def logarithm(x, base=10):
    """Returns the logarithm of x with the given base."""
    if x <= 0:
        raise ValueError("Logarithm only defined for positive numbers!")
    return math.log(x, base)

def natural_log(x):
    """Returns the natural logarithm of x."""
    if x <= 0:
        raise ValueError("Natural logarithm only defined for positive numbers!")
    return math.log(x)

def main():
    print("Select operation:")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Absolute Value")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Logarithm")
    print("12. Natural Log")
    
    choice = input("Enter choice(1/2/3/.../12l): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"The result is: {divide(num1, num2)}")
            except ValueError as e:
                print(e)
    elif choice == '5':
        num1 = float(input("Enter the base number: "))
        num2 = float(input("Enter the exponent: "))
        print(f"The result is: {power(num1, num2)}")
    elif choice == '6':
        num = float(input("Enter the number: "))
        try:
            print(f"The result is: {square_root(num)}")
        except ValueError as e:
            print(e)
    elif choice == '7':
        num = float(input("Enter the number: "))
        print(f"The result is: {absolute_value(num)}")
    elif choice == '8':
        num = float(input("Enter the number (in radians): "))
        print(f"The result is: {sine(num)}")
    elif choice == '9':
        num = float(input("Enter the number (in radians): "))
        print(f"The result is: {cosine(num)}")
    elif choice == '10':
        num = float(input("Enter the number (in radians): "))
        print(f"The result is: {tangent(num)}")
    elif choice == '11':
        num = float(input("Enter the number: "))
        base = float(input("Enter the base: "))
        try:
            print(f"The result is: {logarithm(num, base)}")
        except ValueError as e:
            print(e)
    elif choice == '12':
        num = float(input("Enter the number: "))
        try:
            print(f"The result is: {natural_log(num)}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()