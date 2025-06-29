import csv
from datetime import datetime
from database import init_db, get_db_connection

filename = 'expenses.csv'

# add expense function
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ") or datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category: ") or "Mobile"
    amount = input("Enter amount: ") or "1500"
    note = input("Enter note: ") or "Buy mobile phone"

    conn, cur = get_db_connection()
    cur.execute(
        "INSERT INTO expenses (date, category, amount, note) VALUES (?, ?, ?, ?)",
        (date, category, amount, note)
    )
    conn.commit()
    conn.close()

    print("Expense added successfully!")

# show expenses function
def show_expenses():
    print("\n Show all the expenses: \n")
    conn, cur = get_db_connection()
    cur.execute("SELECT date, category, amount, note FROM expenses")
    rows = cur.fetchall()
    conn.close()
    for row in rows:
        print(f" Date: {row['date']}, Category: {row['category']}, Amount: {row['amount']}, Note: {row['note']}")

# summary function
def summary():
    totals = {}
    total_amount = 0
    print("\n Summary of expenses: \n")
    conn, cur = get_db_connection()
    cur.execute("SELECT category, SUM(amount) as total FROM expenses GROUP BY category")
    rows = cur.fetchall()
    conn.close()
    # print( [ dict(row) for row in rows ] )
    print("Category Totals:")
    for row in rows:
        category = row['category']
        total = row['total']
        totals[category] = total
        total_amount += total
        print(f"Category: {category}, Total: {total}")
    print(f"Total Amount Spent: {total_amount}")

# search expense function
def search_expense():
    keyword = input("Enter keyword to search: ")
    found = False
    conn, cur = get_db_connection()
    cur.execute("SELECT date, category, amount, note FROM expenses")
    rows = cur.fetchall()
    conn.close()
    print("\n Search results: \n")
    for row in rows:
        if keyword.lower() in row['category'].lower() or keyword.lower() in row['note'].lower():
            print(f"Date: {row['date']}, Category: {row['category']}, Amount: {row['amount']}, Note: {row['note']}")
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
