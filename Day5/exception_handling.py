"""try:
    inp = int(input("Enter a number: "))
    print(inp)
except ValueError:
    print("Invalid number")"""

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter denominator: "))
    print(a/b)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("division by zero not possible")