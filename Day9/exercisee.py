"""Create a dictionary comprehension where:

the key is the number
the value is "Even" if the number is even
the value is "Odd" if the number is odd"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = {i:"Even" if i%2==0 else "Odd" for i in numbers}
print(even)

"""
| Type              | Pattern                                                                      |
| ----------------- | ---------------------------------------------------------------------------- |
| List              | `[expression for item in iterable]`                                          |
| List + filter     | `[expression for item in iterable if condition]`                             |
| Dictionary        | `{key: value for item in iterable}`                                          |
| Set               | `{expression for item in iterable}`                                          |
| Conditional value | `{key: value_if_true if condition else value_if_false for item in iterable}` |
"""