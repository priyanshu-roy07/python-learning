"""import math_operations

print(math_operations.add(20, 10))
print(math_operations.subtract(20, 10))
print(math_operations.multiply(20, 10))"""

"""from math_operations import add, subtract, multiply
# from math_operations import *             # it imports all functions from module

print(add(20, 10))
print(subtract(20, 10))
print(multiply(20, 10))"""

#NOTE - We can give the module an 'alias' when module name is long
"""import math_operations as math_op
print(math_op.add(20, 10))
print(math_op.subtract(20, 10))
print(math_op.multiply(20, 10))"""


#Practice
"""import math

print(math.sqrt(144))
print(math.pow(5,3))
print(math.pi)
print(dir(math))"""


#CHALLENGE

from student_utils import calculate_average, is_pass
marks = [75, 82, 68, 90]
average = calculate_average(marks)
print(average)
print(is_pass(average))