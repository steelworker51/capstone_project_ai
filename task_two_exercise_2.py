from datetime import datetime

def add_transaction(transactions):
    """Add a new transaction from user input."""
    print("\n--- Add New Transaction ---")

    # Validate date
    while True:
        date_input = input("Enter date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_input, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    # Customer ID
    customer_id = input("Enter customer ID: ")

    # Validate amount
    while True:
        amount_input = input("Enter amount: ")
        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("Amount must be a number.")

    # Validate transaction type
    while True:
        trans_type = input("Enter type (debit/credit): ").lower()
        if trans_type in ['debit', 'credit']:
            break
        else:
            print("❌ Invalid type. Please enter 'debit' or 'credit'.")

    # Description
    description = input("Enter description: ")

    # Generate ID
    transaction_id = len(transactions) + 1

    # Create and store transaction
    transaction = {
        'transaction_id': transaction_id,
        'date': date.strftime("%Y-%m-%d"),
        'customer_id': customer_id,
        'amount': amount,
        'type': trans_type,
        'description': description
    }

    transactions.append(transaction)
    print("✅ Transaction added successfully.\n")


def view_transactions(transactions):
    """Display transactions in a table, with optional filter by type."""
    print("\n--- View Transactions ---")

    # Ask user if they want to filter
    filter_type = input("Filter by type? (debit/credit/all): ").lower()

    # Validate filter input
    while filter_type not in ['debit', 'credit', 'all']:
        print("❌ Invalid filter option.")
        filter_type = input("Filter by type? (debit/credit/all): ").lower()

    # Filter
    if filter_type != 'all':
        filtered = [t for t in transactions if t['type'] == filter_type]
    else:
        filtered = transactions

    if not filtered:
        print("No transactions found for that filter.")
        return

    # Header
    print(f"\n{'ID':<5} {'Date':<12} {'Customer':<12} {'Amount':<10} {'Type':<8} Description")
    print("-" * 60)

    # Rows
    for t in filtered:
        print(f"{t['transaction_id']:<5} {t['date']:<12} {t['customer_id']:<12} "
              f"{t['amount']:<10.2f} {t['type']:<8} {t['description']}")

    print(f"\nTotal transactions shown: {len(filtered)}\n")


# === MAIN MENU ===
if __name__ == '__main__':
    transactions = [
        {'transaction_id': 1, 'date': '2025-05-24', 'customer_id': 'murphy1', 'amount': 300.0, 'type': 'debit', 'description': 'TV'},
        {'transaction_id': 2, 'date': '2025-05-25', 'customer_id': 'murphy2', 'amount': 100.0, 'type': 'debit', 'description': 'Shoes'},
        {'transaction_id': 3, 'date': '2025-05-26', 'customer_id': 'murphy3', 'amount': 200.0, 'type': 'credit', 'description': 'Refund'},
        {'transaction_id': 4, 'date': '2025-05-27', 'customer_id': 'murphy4', 'amount': 50.0, 'type': 'debit', 'description': 'Snacks'},
        {'transaction_id': 5, 'date': '2022-05-26', 'customer_id': 'murphy5', 'amount': 25.0, 'type': 'credit', 'description': 'Game'},
        {'transaction_id': 6, 'date': '2022-05-27', 'customer_id': 'murphy6', 'amount': 5.0, 'type': 'debit', 'description': 'Movie'}
    ]

    while True:
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_transaction(transactions)
        elif choice == '2':
            view_transactions(transactions)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")


#lines 56-87 prompts the user to filter by debit, credit, or all uses a list comprehension to filter the transactions
#shows only the matching transaction (or message if none match)