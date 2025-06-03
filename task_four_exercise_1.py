from datetime import datetime

def add_transaction(transactions):
    """Add a new transaction from user input."""
    print("\n--- Add New Transaction ---")
    
    # Input and validation for date
    while True:
        date_input = input("Enter date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_input, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    # Input for customer ID (no validation for now)
    customer_id = input("Enter customer ID: ")

    # Input and validation for amount
    while True:
        amount_input = input("Enter amount: ")
        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("Amount must be a number.")

    # Input and validation for type
    while True:
        trans_type = input("Enter type (debit/credit): ").lower()
        if trans_type in ['debit', 'credit']:
            break
        else:
            print("Type must be 'debit' or 'credit'.")

    # Input for description
    description = input("Enter description: ")

    # Generate transaction ID
    transaction_id = len(transactions) + 1

    # Create and append transaction
    transaction = {
        'transaction_id': transaction_id,
        'date': date.strftime("%Y-%m-%d"),
        'customer_id': customer_id,
        'amount': amount,
        'type': trans_type,
        'description': description
    }

    transactions.append(transaction)
    print("Transaction added successfully.\n")


def view_transactions(transactions):
    """Display transactions in a table."""
    if not transactions:
        print("No transactions to show.\n")
        return

    print("\n--- Transactions ---")
    print(f"{'ID':<5}{'Date':<12}{'Customer':<12}{'Amount':<10}{'Type':<8}{'Description'}")
    print("-" * 60)

    for t in transactions:
        print(f"{t['transaction_id']:<5}{t['date']:<12}{t['customer_id']:<12}{t['amount']:<10.2f}{t['type']:<8}{t['description']}")
    print()

def show_highest_debit_customer(transactions):
    """Display the customer with the highest total debit amount."""
    if not transactions:
        print("No transactions available.")
        return

    debit_totals = {}
    for t in transactions:
        if t['type'] == 'debit':
            cid = t['customer_id']
            debit_totals[cid] = debit_totals.get(cid, 0) + t['amount']

    if not debit_totals:
        print("No debit transactions found.")
        return

    highest_customer = max(debit_totals, key=debit_totals.get)
    highest_amount = debit_totals[highest_customer]

    print("\n--- Customer with Highest Total Debit ---")
    print(f"Customer ID: {highest_customer}")
    print(f"Total Debit Amount: ${highest_amount:.2f}\n")


if __name__ == '__main__':
    transactions = [
        {'transaction_id': 1, 'date': '2025-05-24', 'customer_id': 'murphy1', 'amount': 300.0, 'type': 'debit', 'description': 'TV'},
        {'transaction_id': 2, 'date': '2025-05-25', 'customer_id': 'murphy2', 'amount': 100.0, 'type': 'debit', 'description': 'Shoes'},
        {'transaction_id': 3, 'date': '2025-05-26', 'customer_id': 'murphy3', 'amount': 200.0, 'type': 'credit', 'description': 'Refund'},
        {'transaction_id': 4, 'date': '2025-05-27', 'customer_id': 'murphy4', 'amount': 50.0, 'type': 'debit', 'description': 'Snacks'}
    ]

    while True:
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Show Customer with Highest Debit Amount")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_transaction(transactions)
        elif choice == '2':
            view_transactions(transactions)
        elif choice == '3':
            show_highest_debit_customer(transactions)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

# lines 70-91 code for show the customer with the highest debit amount
# lines 100 add the functionality for the customer with the highest debit amount in the menu adding elif choice three for the show_highest_debit_customer function
# lines 96-99 added dictionary info for testing purposes
