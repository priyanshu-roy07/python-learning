"""file = open("notes.txt", "w")
file.write("Python!")
file.close()

file = open("notes.txt", "a")
file.write("\nFile handling.")
file.close()
"""
"""file = open("notes.txt", "r")
print(file.read())
file.close()"""

"""with open("notes.txt", "r") as file:
    #print(file.readline())               #one line    → string
    print(file.readlines())               #all lines   → list
    #print(file.read())                   #entire file → string
"""
"""with open("notes.txt", "r") as file:
    lines = file.readlines()
print(lines[0])"""
#for line in lines:
 #   print(line)


#file = open("students.txt", "w")
#file.write("Priyanshu\nAman\nRahul")
#file.close()

"""with open("students.txt", "w") as file:
    file.write("Priyanshu\nAman\nRahul\n")

with open("students.txt", "a") as file:
    file.write("Rohit\n")

with open("students.txt", "r") as file:
    for line in file:
        print(line, end="")"""

#EXCEPTION HANDLING FOR FILE NOT FOUND ERROR

"""try:
    with open("unknown.txt", "r") as file:
        for line in file:
            print(line, end="")
except FileNotFoundError:
    print("File not found!")"""


#JSON

import json

student = {
    "name" : "Priyanshu",
    "age" : 22,
    "city" : "Delhi"
}
#NOTE
#json.dump() → Python → JSON
#json.load() → JSON → Python

with open("student.json", "w") as file:
    json.dump(student, file, indent= 4)

with open("student.json", "r") as file:
    student = json.load(file)

print(student)
print(student["name"])
print(student["city"])

