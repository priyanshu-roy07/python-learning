"""num1 = int(input("Enter first number: "))

op = input("Enter operator (+, -, *, /, %, **, //): ")

num2 = int(input("Enter second number: "))

if op =="+":
    print(num1 + num2)
elif op =="-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "%":
    print(num1 % num2)
elif op == "**":
    print(num1 ** num2)
elif op == "//":
    print(num1 // num2)
else:
    print("Invalid operator")"""

#CALCULATOR USING FUNCTIONS

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def modulo(a,b):
    return a % b

def power(a,b):
    return a ** b

def floor_division(a,b):
    return a // b