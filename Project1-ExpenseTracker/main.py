expenses = []

def add_expense():

    expense = {
        "description" : input("Enter description: "),
        "amount" : int(input("Enter amount: ")),
        "category" : input("Enter category: ")
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
    search_term = input("Enter what to search: ").lower() 
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
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")