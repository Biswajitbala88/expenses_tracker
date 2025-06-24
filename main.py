import csv
from datetime import datetime

filename = 'expenses.csv'

# add expense function
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    note = input("Enter note: ")

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            date,
            category,
            amount,
            note
        ])

    print("Expense added successfully!")

# show expenses function
def show_expenses():
    print("\n Show all the expenses: \n")

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # lists = list(reader)
        # print(lists)
        for row in reader:
            print(f"Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Note: {row[3]}")

# summary function
def summary():
    totals = {}
    total_amount = 0
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # lists = list(reader)
        # print(lists)
        for row in reader:
            category = row[1]
            amount = float(row[2])
            totals[category] = totals.get(category, 0) + amount
            total_amount += amount
        print(totals.items())

        for category, total in totals.items():
            print(f"Category: {category}, Total: {total}")
        print(f"  Total: {total_amount}") 

def menu():
    while True:
        print("\n Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()