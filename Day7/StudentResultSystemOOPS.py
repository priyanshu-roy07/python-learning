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

students = [student1, student2, student3]

student2.update_marks([56,44,65])

for student in students:
    student.display_info()
    print(f"Average of marks: {student.calculate_average()} -> {student.calculate_grade()}")

class StudentManager:
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)

student1 = student()
manager = StudentManager()
print(manager.students)