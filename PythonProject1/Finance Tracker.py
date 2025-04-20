from datetime import datetime
import json

try:
    with open("finance_history.json") as f:
        transaction_list = json.load(f)
except json.JSONDecodeError:
    print("Warning: JSON file is empty or corrupted. Starting with an empty transaction list.")
    transaction_list = []


def display_menu():
    print("----- Finance Tracker Menu -----")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Balance")
    print("5. Exit")

balance = 0
def add_transaction(type):
    amount = float(input("Enter the amount of the transaction: $"))
    category = input("Enter the category of the transaction: ")
    date = datetime.now().strftime("%m/%d/%Y")

    transaction = {'Type': type,
                   'Amount': amount,
                   'Category': category,
                   'Date': date}

    transaction_list.append(transaction)
    with open("finance_history.json", "w") as f:
        json.dump(transaction_list, f)

def view_transactions():
    for transaction in transaction_list:
        print("----- Transaction Details -----")
        print("Transaction Type: ", transaction.get('Type'))
        print("Amount: ", transaction.get('Amount'))
        print("Category: ", transaction.get('Category'))
        print("Date: ", transaction.get('Date'))
        print()

def view_balance():
    balance = 0
    print("----- Balance Details -----")
    for transaction in transaction_list:
        if transaction['Type'] == "Income":
            balance += transaction['Amount']
        elif transaction['Type'] == "Expense":
            balance -= transaction['Amount']
    print("Balance: ", balance)
    print()


while True:
    display_menu()
    choice = input("Enter your choice (1 - 5): ")

    if choice == "1":
        add_transaction("Income")
    elif choice == "2":
        add_transaction("Expense")
    elif choice == "3":
        view_transactions()
    elif choice == "4":
        view_balance()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please select 1-5.")



