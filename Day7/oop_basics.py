"""class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student1 = Student("Priyanshu", 98)     #student1 and student2 are objects of class Student
student2 = Student("Aman", 89)          # self -> student2

print(student1.name, student1.marks)
print(student2.name, student2.marks)
"""

#PRACTICE
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "City", 2024)

print(car1.brand, car1.model, car1.year)
print(car2.brand, car2.model, car2.year)