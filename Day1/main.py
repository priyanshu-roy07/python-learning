import mini_calculator

try:
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    op = input("Enter operator (+, -, *, /, %, **, //): ")

    if op =="+":
        addition = mini_calculator.add(a,b)
        print(addition)
    elif op =="-":
        sub = mini_calculator.subtract(a,b)
        print(sub)
    elif op == "*":
        multiplication = mini_calculator.multiply(a,b)
        print(multiplication)
    elif op == "/":
        division = mini_calculator.divide(a,b)
        print(division)
    elif op == "%":
        mod = mini_calculator.modulo(a,b)
        print(mod)
    elif op == "**":
        power_result = mini_calculator.power(a,b)
        print(power_result)
    elif op == "//":
        flr_division = mini_calculator.floor_division(a,b)
        print(flr_division)
    else:
        print("Invalid operator")

except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")