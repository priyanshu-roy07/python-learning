"""def introduce(name, age, country="India"):
    print(f"My name is {name}, I'm {age} years old and I'm from {country}")

introduce(country="Germany", age=25, name="Rahul")"""

#GLOBAL KEYWORD
"""count = 0
def increase():
    global count
    count = count + 1
increase()
increase()
increase()
print(count)"""

#*ARGS - WHEN A FUNCTION DON'T HAVE A FIXED NUMBER OF PARAMETERS
#Collects positional arguments into a tuple:

"""def calc_sum(*args):
    total = 0
    for number in args:
        total = total + number
    return total
print(calc_sum(10, 20, 30))

def calculate_sum(*args):
    print(args)
calculate_sum(10, 20, 30, 40)"""

#**KWARGS - When we don't know how many keyword arguments the function will receive
#Collects keyword arguments into a dictionary:

"""def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
show_profile(name="Priyanshu", age=22, job="Engineer")"""

#LAMBDA         lambda arguments : expression

#def double(x):
#    return x * 2
"""double = lambda x : x*2
print(double(5))

square = lambda x : x**2
print(square(9))"""

#map()          map(function, collection)

"""numbers = [2, 4, 6, 8, 10]

triplee = map(lambda x : x*3, numbers)
triple = list(map(lambda x : x*3, numbers))         #converted into list
print(triplee)
print(triple)"""

#filter()

"""numbers = [5, 12, 7, 20, 3, 18, 9]
num = list(filter(lambda x : x > 10, numbers))
print(num)"""

#sorted()

students = [
    {"name": "Rahul", "marks": 85},
    {"name": "Priyanshu", "marks": 92},
    {"name": "Amit", "marks": 78},
    {"name": "Neha", "marks": 88}
]

studentss = sorted(students, 
                   key= lambda student : student["marks"],
                   reverse= True)
for student in studentss:
    print(student["name"], "->", student["marks"])