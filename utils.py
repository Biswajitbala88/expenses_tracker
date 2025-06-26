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

# search expense function
def search_expense():
    keyword = input("Enter keyword to search: ")
    found = False
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if keyword.lower() in row[1].lower() or keyword.lower() in row[3].lower():
                print(f"Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Note: {row[3]}")
                found = True
    if not found:
        print("No expenses found with that keyword.")

# edit expense function
def edit_expense():
    date  = input("Enter the date of the expense to edit (YYYY-MM-DD): ")
    found = False
    expenses = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == date:
                found = True
                print(f"Current details: Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Note: {row[3]}")
                new_category = input("Enter new category (leave blank to keep current): ") or row[1]
                new_amount = input("Enter new amount (leave blank to keep current): ") or row[2]
                new_note = input("Enter new note (leave blank to keep current): ") or row[3]
                expenses.append([date, new_category, new_amount, new_note])
            else:
                expenses.append(row)
    if found:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(expenses)
        print("Expense updated successfully!")
    else:
        print("Expense not found for the given date.")

# delete expense function
def delete_expense():
    date = input("Enter the date of the expense to delete (YYYY-MM-DD): ")
    found = False
    expenses = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        header = rows[0]
        data_rows = rows[1:]

        matching = [row for row in data_rows if row[0] == date]

        if not matching:
            print("Expense not found for the given date.")
            return

        print(f"\nFound {len(matching)} record(s) on {date}:")
        for i, row in enumerate(matching, 1):
            print(f"{i}. Category: {row[1]}, Amount: ₹{row[2]}, Note: {row[3]}")

        try:
            choice = int(input("Enter the number of the record to delete: ")) - 1
            if 0 <= choice < len(matching):
                record_to_delete = matching[choice]
                data_rows.remove(record_to_delete)
                found = True
            else:
                print("Invalid selection.")
                return
        except ValueError:
            print("Invalid input.")
            return

    if found:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data_rows)
        print("🗑️ Expense deleted successfully!")
