import datetime

# Data structure to store expenses
expenses = []

# Function to add an expense
def add_expense():
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the expense category: ")
    description = input("Enter a brief description: ")
    date = datetime.date.today()
    
    expenses.append({
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    })
    print("Expense added successfully!")

# Function to list expenses
def list_expenses():
    if not expenses:
        print("No expenses recorded.")
    else:
        print("List of Expenses:")
        for expense in expenses:
            print(f"Date: {expense['date']} | Amount: ${expense['amount']} | Category: {expense['category']} | Description: {expense['description']}")

# Main menu loop
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        list_expenses()
    elif choice == "3":
        print("Exiting the Expense Tracker.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
