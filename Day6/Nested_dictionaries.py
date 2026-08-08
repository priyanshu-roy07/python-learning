#Normal Dictionaries
"""students = {
    "Rahul" : 85,
    "Aman" : 97,
    "Priyanshu" : 99
}
print(students["Priyanshu"])
for keys, values in students.items():
    print(keys, values)"""

#Nested Dctionaries

"""students = {
    "Priyanshu" : {
        "age" : 22,
        "marks" : 98,
        "branch" : "CSE"
    },

    "Aman" : {
        "age" : 26,
        "marks" : 95,
        "branch" : "AIML"
    },

    "Bumba" : {
        "age" : 24,
        "marks" : 87,
        "branch" : "CSE"
    }
}

#print(students["Priyanshu"]["marks"])
#print(students["Aman"]["branch"])

for keys, values in students.items():
    print(keys, students[keys]["marks"])"""


#FUNCTIONS (IN-DEPTH)

"""def add(a, b):
    print(a + b)
add(10,5)           #function call

def add1(a, b):         #MULTIPLE ARGUMENTS ---> a,b
    return a + b
result = add1(20, 10)
print(result)"""

#PARAMETERS AND ARGUMENTS

"""def greet(name):            # name ---> parameter
    print("Hello", name)
greet("Priyanshu")"""          # "Priyanshu" --> argument

#DEFAULT ARGUMENT
"""def greet(name = "User"):
    print("Hello", name)
greet()             """           #FUNCTION CALL

#PRACTICE
"""def calc_avg(a, b, c):
    result = (a + b + c)/3
    return result
result = calc_avg(10,20,30)
print(result)"""

#SCOPE
"""x = 10

def test():
    x = 20
    print(x)
test()      # x = 20 (Local Scope)
print(x)        #x = 10 (Global scope)"""

#PRACTICE 2
"""def check_result(marks):
    if marks >= 40:
        return "Pass"
    return "Fail"       #No need of else statement
result = check_result(12)
print(result)"""

#PRACTICE 3
"""numbers = [10, 45, 23, 89, 12]

def find_highest(numbers):
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    print(max)
find_highest(numbers)"""