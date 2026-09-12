"""
Iterable → list, tuple, string, etc.
iter() → creates an iterator from an iterable.
Iterator → remembers its current position.
next() → gets the next item.
StopIteration → happens when there are no more items.
Creating a new iterator starts from the beginning again.
"""

"""numbers = [10, 20, 30]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))"""


"""numbers = [10, 20, 30]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))

iterator = iter(numbers)
print(next(iterator))"""


"""name = "Python"
iterator = iter(name)
print(next(iterator))
print(next(iterator))
print(next(iterator))"""

#Dictionary
"""student = {
    "name": "Priyanshu",
    "age": 22,
    "marks": 90
}
iterator = iter(student)
print(next(iterator))  # name
print(next(iterator))  # age"""


num = [5,10,15,20,25]
iterator = iter(num)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
