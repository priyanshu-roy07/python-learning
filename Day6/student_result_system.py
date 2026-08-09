def calculate_average (marks):
    total = 0
    for mark in marks:
        total += mark
    return total/len(marks)

def find_highest(marks):
    highest = marks[0]

    for mark in marks:
        if mark > highest:
            highest = mark

    return highest

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
        
    elif choice == "2":
        for name, details in students.items():
            print(name,"->", details["marks"])

    elif choice == "3":
        search = input("Enter student name: ")

        if search in students:
            marks = students[search]["marks"]
            average = calculate_average(marks)
            print("Average marks: ",average)
        else:
            print("Student not found!")

    elif choice == "4":
        search = input("Enter student name: ")

        if search in students:
            marks = students[search]["marks"]
            highest = find_highest(marks)
            print("Highest marks:", highest)

        else:
            print("Student not found")
    elif choice == "5":
            search = input("Enter student to search: ")
            if search in students:
                print("Student found")
            else:
                print("Student not found!")
    elif choice == "6":
        print("Thankyou!")
        break
    else:
        print("Invalid choice!")