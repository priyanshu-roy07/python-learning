while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /, %, **, //): ")
    def add(num1, num2):
        return num1 + num2
    def subtract(num1, num2):
        return num1 - num2
    def multiply(num1, num2):
        return num1*num2
    def divide(num1, num2):
        return num1/num2
    def modulo(num1, num2):
        return num1 % num2
    def exponantion(num1, num2):
        return num1 ** num2
    def floor_division(num1, num2):
        return num1 // num2

    if operator == "+":
        print(f"The sum of {num1} and {num2} is {add(num1, num2)}")
    elif operator == "-":
        print(f"The difference of {num1} and {num2} is {subtract(num1, num2)}")
    elif operator == "*":
        print(f"The product of {num1} and {num2} is {multiply(num1, num2)}")
    elif operator == "/":
        print(f"The quotient of {num1} and {num2} is {divide(num1, num2)}")
    elif operator == "%":
        print(f"The remainder of {num1} and {num2} is {modulo(num1, num2)}")
    elif operator == "**":
        print(f"The result of {num1} raised to the power of {num2} is {exponantion(num1, num2)}")
    elif operator == "//":
        print(f"The floor division of {num1} and {num2} is {floor_division(num1, num2)}")
    else:
        print("Invalid operator")

    choice = input("Wanna calculate again? y/n: ")
    if choice == "n":
        break

print("Thanks for using the calculator.")