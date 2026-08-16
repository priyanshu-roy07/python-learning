class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_info(self):
        print(self.name, self.marks)
    def calculate_average(self):
        return sum(self.marks)/len(self.marks)
    def calculate_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >=80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "Fail"
    def update_marks(self, new_marks):
        self.marks = new_marks

class StudentManager:
    def __init__(self):
        self.students = []
        
    def add_student(self, student):
        self.students.append(student)
    def view_students(self):
        for student in self.students:
            student.display_info()
            print(f"Average of marks: {student.calculate_average()} -> {student.calculate_grade()}")
    def search_students(self, search_name):
        found = False
        for student in self.students:
            if search_name == student.name:
                student.display_info()
                print(f"Average of marks: {student.calculate_average()} -> Grade {student.calculate_grade()}")
                print("Student found!")
                found = True
        if found is False:
            print("Student not found!")
    def update_student_marks(self, student_name, new_marks):
        found = False
        for student in self.students:
            if student_name == student.name:
                student.update_marks(new_marks)
                found = True
        if found is False:
            print("Student not found!")
    def remove_student(self, student_name):
        found = False
        for student in self.students:
            if student_name == student.name:
                self.students.remove(student)
                found = True
        if found is False:
            print("Student not found!")
    def find_highest(self):
        if not self.students:
            print("No student in the list!")
        else:
            highest = self.students[0]
            for student in self.students:
                if student.calculate_average() > highest.calculate_average():
                    highest = student
            return highest

manager = StudentManager()

while True:
    print("\n===== STUDENT RESULT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Remove Student")
    print("6. Find Highest")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        
        marks = []
        
        marks.append(int(input("Enter mark1: ")))
        marks.append(int(input("Enter mark2: ")))
        marks.append(int(input("Enter mark3: ")))

        new_student = Student(name, marks)
        manager.add_student(new_student)

    elif choice == "2":
        manager.view_students()

    elif choice == "3":
        name = input("Enter student name to search: ")
        manager.search_students(name)

    elif choice == "4":
        name = input("Enter student name: ")
                
        new_marks = []
                
        new_marks.append(int(input("Enter mark1: ")))
        new_marks.append(int(input("Enter mark2: ")))
        new_marks.append(int(input("Enter mark3: ")))

        manager.update_student_marks(name, new_marks)

    elif choice == "5":
        name = input("Enter student name: ")
        manager.remove_student(name)

    elif choice == "6":
        highest = manager.find_highest()
        print(f"Student with highest marks: {highest.name} \n His marks average : {highest.calculate_average()}\n Grade: {highest.calculate_grade()}")

    elif choice == "7":
        print("Thankyou!")
        break