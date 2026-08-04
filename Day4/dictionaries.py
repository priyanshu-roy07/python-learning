"""student = {
    "name": "Priyanshu",
    "age": 23,
    "branch": "CSE",
    "marks": 92
}
student["marks"] = 98
student["college"] = "SU"

print(student["college"])"""

"""student = {
    "name": "Priyanshu",
    "age": 23
}
print(len(student))"""

# MINI CHALLENGE
"""employee = {
    "id": 101,
    "name": "Alice",
    "salary": 50000,
    "department": "IT"
}
employee["salary"] = 55000
employee['city'] = "Banglore"
print(f"Name of the employee is {employee["name"]} and salary is {employee['salary']}")
print(employee.keys())
print(employee.values())"""

# MINI PROJECT - Student Database
students = {}

while True:
    name = input("Enter your name: ")
    marks = int(input("Enter your marks: "))
    students[name] = marks
    choice = input("Add another? y/n ")
    if choice == "n":
        break
for key, value in students.items():
    print(key,":", value)