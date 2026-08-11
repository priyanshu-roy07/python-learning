"""class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student1 = Student("Priyanshu", 98)     #student1 and student2 are objects of class Student
student2 = Student("Aman", 89)          # self -> student2

print(student1.name, student1.marks)
print(student2.name, student2.marks)
"""


#NOTE: Function → independent
#      Method   → function belonging to a class/object 

#PRACTICE
"""class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):             #Method used here (A method is simply a function that belongs to a class/object.)
        print(self.brand, self.model, self.year)


car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "City", 2024)

car1.display_info()         #printing directly using method created earlier
car2.display_info()

#print(car1.brand, car1.model, car1.year)
#print(car2.brand, car2.model, car2.year)"""

#EXERCISE

"""class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def display_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")
    def deposit(self, amount):
        self.balance += amount
        #print(f"{self.owner}'s balance: {self.balance}")
    def withdraw(self, amount):
        self.balance -= amount
        #print(f"{self.owner}'s balance: {self.balance}")

account_details = BankAccount("Priyanshu", 50000)

account_details.display_balance()
account_details.deposit(10000)
account_details.display_balance()
account_details.withdraw(5000)
account_details.display_balance()
"""

#ENCAPSULATION
#Encapsulation means controlling how the internal data of an object can be accessed or changed.

"""class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
    def display_balance(self):
        print(f"{self.owner}'s balance: {self._balance}")
    def deposit(self, amount):
        self._balance += amount
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient balance!")

account_details = BankAccount("Priyanshu", 50000)

account_details.display_balance()

account_details.deposit(10000)
account_details.display_balance()

account_details.withdraw(5000)
account_details.display_balance()

account_details.withdraw(60000)
account_details.display_balance()"""


#INHERITANCE
#Inheritance is a mechanism in object-oriented programming that allows a class (called the child or subclass) to inherit properties and behaviors (attributes and methods) from another class (called the parent or superclass). This promotes code reusability and establishes a hierarchical relationship between classes.

"""class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
    def display_info(self):
        print(f"Student: {self.name}, roll no. {self.roll_number}")

class Engineering_student(Student):
    def __init__(self,name, roll_number, programming_language):
        super().__init__(name, roll_number)
        self.programming_language = programming_language
    def display_specialization(self):
        print(self.programming_language)

student1 = Engineering_student("Priyanshu", 7, "Python")

student1.display_info()
student1.display_specialization()"""


#POLYMORPHISM
#Polymorphism is a concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different types of objects, allowing for flexibility and code reusability.

class Student:
    def display_info(self):
            print("General student course")

class EngineeringStudent(Student):
    def display_info(self):
        print("Computer Science Engineering")

class MedicalStudent(Student):
        def display_info(self):
            print("Medicine")

student1 = EngineeringStudent()
student2 = MedicalStudent()

students = [student1, student2]

for student in students:
     student.display_info()

#student1.display_info()
#student2.display_info()