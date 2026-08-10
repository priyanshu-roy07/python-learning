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

class BankAccount:
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
account_details.display_balance()