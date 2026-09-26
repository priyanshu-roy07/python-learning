import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "expenses.json"

expenses = []

def add_expense():
    description = input("Enter description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return

    try:
        amount = int(input("Enter amount: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return
    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    category = input("Enter category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return
    
    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    print("Expense added successfully")

def view_expenses():
    if not expenses:
        print("No expenses found!")
    else:
        for number, items in enumerate(expenses, start=1):
                print(f"{number} -> {items['description']} | {items['amount']} | {items['category']}")

def search_expenses(): 
    search_term = input("Enter what to search: ").strip().lower()
    found = False 
    if not expenses: 
        print("No expenses found!")
    else: 
        for number, items in enumerate(expenses, start=1): 
            if ( search_term in items["description"].lower() or search_term in items["category"].lower() ): 
                print( f"{number} -> " f"{items['description']} | " f"{items['amount']} | " f"{items['category']}" ) 
                found = True 
        if not found: 
            print("No matching expenses found!")

def delete_expense():
    try:
        search_item = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Invalid expense number! Please enter a number.")
        return

    if not expenses:
        print("No expenses found!")
        return
    if search_item < 1 or search_item > len(expenses):
        print("Invalid expense number!")
        return
    deleted_expense = expenses.pop(search_item - 1)
    print("Expense deleted successfully!")

def total_spending():
    total = 0

    if not expenses:
        print("No expenses found!") 
    else:
        for items in expenses:
            total = total + items['amount']
        print(f"Total spending : {total}")

def spending_by_category():
    category_totals = {}
    if not expenses:
            print("No expenses found!") 
    else:
        for items in expenses: 
            category = items['category']
            amount = items['amount']
            if category in category_totals:
                category_totals[category] = category_totals[category] + amount
            else:
                category_totals[category] = amount
        for category, total in category_totals.items():
            print(f"{category}: {total}")

def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)
    print("Data saved successfully!")

def load_data():
    global expenses
    try:
        with open(DATA_FILE, "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        print("No saved expenses found. Starting with an empty list.")
    except json.JSONDecodeError:
        print("Saved data is corrupted. Starting with an empty list.")

load_data()

while True:
    print("1. Add expense")
    print("2. View expenses")
    print("3. Search expenses")
    print("4. Delete expense")
    print("5. Show total spending")
    print("6. Show spending by category")
    print("7. Save data")
    print("8. EXIT")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        search_expenses()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        total_spending()
    elif choice == "6":
        spending_by_category()
    elif choice == "7":
        save_data()
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")