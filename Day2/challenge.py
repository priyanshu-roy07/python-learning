#LOOPS

#Find the sum of numbers from 1 to 100.
"""total = 0
for i in range(1, 101):
    total += i
    print(f"Current number: {i}, Current total: {total}")
print(f"Final total: {total}")"""

#Ask the user for a number. Count how many digits it contains.

"""num = int(input("Enter a number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print(f"The number contains {count} digits.")"""

#Reverse a number.
num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print(f"The reversed number is: {reversed_num}")