from datetime import datetime
import json
import os

# Load or initialize transaction history
if os.path.exists("finance_history.json"):
    with open("finance_history.json") as f:
        transaction_hist = json.load(f)
else:
    transaction_hist = []

def display_menu():
    print("\n--- Personal Finance Tracker ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Balance")
    print("5. Exit")

def add_transaction(transaction_type):
    amount = float(input("Enter the amount of the transaction: "))
    category = input("Enter the category of the transaction: ")
    date = datetime.now().strftime("%m/%d/%Y")

    transaction = {
        'Type': transaction_type,
        'Amount': amount,
        'Category': category,
        'Date': date
    }

    transaction_hist.append(transaction)

    with open("finance_history.json", "w") as f:
        json.dump(transaction_hist, f, indent=4)

def view_transactions():
    print("\n--- Transaction History ---")
    for t in transaction_hist:
        print(f"{t['Date']} | {t['Type']} | ${t['Amount']} | {t['Category']}")

def view_balance():
    balance = 0
    for t in transaction_hist:
        if t['Type'].lower() == "income":
            balance += t['Amount']
        elif t['Type'].lower() == "expense":
            balance -= t['Amount']
    print(f"\nCurrent Balance: ${balance:.2f}")

# --- Main Loop ---
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_transaction("Income")
    elif choice == "2":
        add_transaction("Expense")
    elif choice == "3":
        view_transactions()
    elif choice == "4":
        view_balance()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-5.")
