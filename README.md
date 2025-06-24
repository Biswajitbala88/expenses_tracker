# 💰 Expense Tracker (CLI-Based Python Project)

A simple, beginner-friendly command-line based **Expense Tracker** built using Python. This app helps you keep track of your daily expenses, categorized by type, with CSV file-based storage for long-term use.

---

## 📌 Features

- ✅ Add a new expense (date, category, amount, optional note)
- ✅ View all stored expenses
- ✅ Summary of total expenses grouped by category
- ✅ Automatically stores expenses in a `CSV` file
- ✅ Easy-to-use command-line menu interface
- ✅ No external libraries required (pure Python)
- ✅ Lightweight, fast, and beginner-friendly

---

## 🧠 Key Skills Used

- Python Functions
- File I/O using CSV
- Data structures (lists, dictionaries)
- CLI interaction
- Date formatting and validation
- Code modularization with helper utilities (`utils.py`)
- Git and GitHub project structure

---

## 🗂 Folder Structure

```
expenses_tracker/
├── main.py          # Main application file with CLI menu
├── utils.py         # (Optional) Utility/helper functions
├── expenses.csv     # Stores the expense records
└── README.md        # Project documentation (this file)
```

---

## 🧰 Requirements

- Python 3.6 or above
- No external dependencies

---

## ▶️ How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Biswajitbala88/expenses_tracker.git
   cd expenses_tracker
   ```

2. **Run the Python script**:
   ```bash
   python main.py
   ```

---

## 🎮 Sample Usage

```bash
💰 Expense Tracker Menu:
1. Add Expense
2. Show Expenses
3. Show Summary
4. Exit

Choose an option: 1
Enter date (YYYY-MM-DD) [leave blank for today]: 2025-06-25
Enter category (e.g., food, travel, bills): food
Enter amount: 120
Enter note (optional): dinner

✅ Expense added successfully!
```

---

## 📊 Example Summary Output

```bash
📊 Summary:
  food: ₹320.0
  travel: ₹180.0
  bills: ₹90.0
  Total: ₹590.0
```

---

## 🚀 Future Improvements

- [ ] Add search, edit, and delete features
- [ ] Filter expenses by date range
- [ ] Monthly report generation
- [ ] Export to PDF or Excel
- [ ] GUI version using Tkinter or PyQt
- [ ] SQLite or JSON-based storage option

---

## 📄 License

This project is licensed under the **MIT License** – you’re free to use, modify, and distribute it with attribution.

---

## 🙌 Author

**Biswajit Bala**  
[GitHub Profile →](https://github.com/Biswajitbala88)

---
