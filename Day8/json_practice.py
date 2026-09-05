import json

student = [
    {
        "name" : "Priyanshu",
        "marks" : 98
    },
    {
        "name" : "Aman",
        "marks" : 88
    },
    {
        "name" : "Bumba",
        "marks" : 86
    }
]

try:
    with open("students.json", "w") as file:
        json.dump(student, file, indent=4)

    with open("students.json", "r") as file:
        student = json.load(file)

    print(student)
    print(student[0]["name"])
    print(student[0]["marks"])

    print(student[1]["name"])
    print(student[1]["marks"])

    print(student[2]["name"])
    print(student[2]["marks"])

except FileNotFoundError:
    print("File not found!")