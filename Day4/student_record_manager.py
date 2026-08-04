#Add students, view all students, search student, exit

students = {}
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks

    if choice == "2":
        for key, value in students.items():
            print(key, ":", value)

    if choice == "3":
        search = input("Enter the student name to search: ")
        if search in students:
            print(f"Marks of {search}: {students[search]}")
        else:
            print("Student not found!")

    if choice == "4":
        print("Thankyou!")
        break