from database import create_table
from expense import add_expense, view_expenses, delete_expense
from report import monthly_summary, category_summary
from tabulate import tabulate

def main_menu():
    create_table()

    while True:
        print("\n==== Personal Expense Tracker ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("4. Monthly Summary")
        print("5. Category-wise Summary")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            note = input("Enter note: ")
            add_expense(amount, category, date, note)
            print("✅ Expense added successfully.")
        elif choice == '2':
            expenses = view_expenses()
            if expenses:
                print(tabulate(expenses, headers=["ID", "Amount", "Category", "Date", "Note"], tablefmt="grid"))
            else:
                print("No expenses found.")
        elif choice == '3':
            expense_id = int(input("Enter Expense ID to delete: "))
            delete_expense(expense_id)
            print("🗑️ Expense deleted.")
        elif choice == '4':
            monthly_summary()
        elif choice == '5':
            category_summary()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
