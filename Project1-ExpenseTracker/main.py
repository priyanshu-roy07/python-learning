import storage
import expense_manager

expenses = storage.load_data()

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
        expense_manager.add_expense(expenses)
    elif choice == "2":
        expense_manager.view_expenses(expenses)
    elif choice == "3":
        expense_manager.search_expenses(expenses)
    elif choice == "4":
        expense_manager.delete_expense(expenses)
    elif choice == "5":
        expense_manager.total_spending(expenses)
    elif choice == "6":
        expense_manager.spending_by_category(expenses)
    elif choice == "7":
        storage.save_data(expenses)
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")


#ARCHITECTURE
"""
main.py
   │
   ├── controls menu
   └── owns expenses
          │
          ├───────────────┐
          ↓               ↓
expense_manager.py     storage.py
   │                      │
   ├── add                ├── save
   ├── view               └── load
   ├── search
   ├── delete
   ├── total
   └── category
"""