from database import create_table
from expense_manager import add_expense, get_expenses, get_total_expenses

create_table()

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        amount = float(input("Amount: "))
        category = input("Category: ")
        date = input("Date (YYYY-MM-DD): ")
        description = input("Description: ")

        add_expense(amount, category, date, description)
        print("Expense added successfully!")

    elif choice == "2":
        expenses = get_expenses()
        for expense in expenses:
            print(expense)

    elif choice == "3":
        total = get_total_expenses()
        print("Total Expenses:", total)

    elif choice == "4":
        break