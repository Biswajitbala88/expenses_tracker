from utils import add_expense, show_expenses, summary, search_expense, edit_expense, delete_expense
from database import init_db

init_db()


def menu():
    while True:
        print("\n Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Show Summary")
        print("4. Search Expense")
        print("5. Edit Expense")
        print("6. Delete Expense")
        print("7. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            summary()
        elif choice == "4":
            search_expense()
        elif choice == "5":
            edit_expense()
        elif choice == "6":
            delete_expense()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()