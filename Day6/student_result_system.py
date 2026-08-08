students = {}

while True:
    print("1. Add student")
    print("2. View Students")
    print("3. Calculate Average")
    print("4. Find highest marks")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter student name: ")

        marks = []

        marks.append(int(input("Enter mark1: ")))
        marks.append(int(input("Enter mark2: ")))
        marks.append(int(input("Enter mark3: ")))

        students[name] = {
            "marks": marks
        }

        print("name:", name)
        print("marks:", marks)
        print("students:", students)
        
        students[name] = students[name][marks]
    """elif choice == "2":
        for name, details in students.items():
            print(name, details["marks"])
    elif choice == "3":
        total = 0
        for mark in marks:
            total += mark
        average = total/len(students)
    elif choice == "4":
        highest = marks[0]
        for mark in marks:
            if mark > highest:
                highest = mark
        print(highest)
    elif choice == "5":
        search = input("Enter student to search: ")
        if search in students:
            print("Student found")
        else:
            print("Not found!")
    elif choice == "6":
        print("Thankyou!")
        break
"""