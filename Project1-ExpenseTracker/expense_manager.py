def add_expense(expenses):
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

def view_expenses(expenses):
    if not expenses:
        print("No expenses found!")
    else:
        for number, items in enumerate(expenses, start=1):
                print(f"{number} -> {items['description']} | {items['amount']} | {items['category']}")

def search_expenses(expenses): 
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

def delete_expense(expenses):
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

def total_spending(expenses):
    total = 0

    if not expenses:
        print("No expenses found!") 
    else:
        for items in expenses:
            total = total + items['amount']
        print(f"Total spending : {total}")

def spending_by_category(expenses):
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