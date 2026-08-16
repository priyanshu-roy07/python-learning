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

student1 = Student("Priyanshu", [98, 95, 94])
student2 = Student("Aman", [89, 78, 86])
student3 = Student("Bumba", [78, 67, 86])

#students = [student1, student2, student3]

#student2.update_marks([56,44,65])

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
manager = StudentManager()
manager.add_student(student1)
manager.add_student(student2)
manager.add_student(student3)
"""manager.search_students("Priyanshu")
#manager.search_students("Shivam")
manager.update_student_marks("Aman", [87, 78, 77])
manager.search_students("Aman")"""
manager.remove_student("Bumba")
manager.view_students()
