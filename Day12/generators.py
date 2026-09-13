#return → give value → function ends
#yield  → give value → pause → resume later

"""def test():
    yield 10
    yield 20
    yield 30
result = test()
print(next(result))
"""
"""
def count_numbers():
    for i in range(1,6):
        yield i
result = count_numbers()
for num in result:
    print(num)
"""

#GENERATOR COMPREHENSIONS
"""
squares = (x ** 2 for x in range(1,6))
for num in squares:
    print(num)
"""
#NOTE - generator is memory-efficient when you only need to process values one at a time.

#PRACTICE

#Create a generator called even_numbers(limit) that produces even numbers from 2 up to the given limit.
"""def even_numbers(limit):
    for number in range(1,limit):
        if number % 2 == 0:
            yield number
result = even_numbers(21)

for num in result:
    print(num)"""

#CHALLENGE2
#If n = 5, what should the loop do to produce 5, 4, 3, 2, 1?
"""def countdown(n):
    for number in range(n,0,-1):
        yield number
result = countdown(5)
for num in result:
    print(num)
"""

#CHALLENGE3
# A generator that reads a list of numbers and yields only the numbers greater than 50, one at a time.
"""numbers = [20, 55, 30, 80, 45, 100, 60]
def above_50(numbers):
    for number in numbers:
        if number > 50:
            yield number
result = above_50(numbers)
for num in result:
    print(num)"""

"""
| `return`                             | `yield`                               |
| ------------------------------------ | ------------------------------------- |
| Gives a value and ends the function  | Gives a value and pauses the function |
| Can normally return one final result | Can produce many values               |
| Function execution stops             | Execution can resume                  |
| Doesn't create a generator           | Creates a generator                   |
"""

#CHALLENGE4
"""def fibonacci(n):
    first = 0 
    second = 1
    for i in range(0,n):
        yield first
        old_first = first
        first = second
        second = old_first + second
result = fibonacci(7)

for num in result:
    print(num)"""

#CHALLENGE5
#EVEN FIBONACCI

def even_fibonacci(n):
    first = 0 
    second = 1
    count = 0 

    while count < n:
        if first % 2 == 0:
            yield first
            count += 1
        old_first = first
        first = second
        second = old_first + second
        
result = even_fibonacci(5)
for num in result:
    print(num)