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


from datetime import datetime

def view_transactions(transactions):
    """Display transactions in a table, with optional filter by type."""
    print("\n--- View Transactions ---")

    filter_type = input("Filter by type? (debit/credit/all): ").lower()

    while filter_type not in ['debit', 'credit', 'all']:
        print("❌ Invalid filter option.")
        filter_type = input("Filter by type? (debit/credit/all): ").lower()

    if filter_type != 'all':
        filtered = [t for t in transactions if t['type'] == filter_type]
    else:
        filtered = transactions

    if not filtered:
        print("No transactions found for that filter.")
        return

    print(f"\n{'ID':<5} {'Date':<15} {'Customer':<12} {'Amount':<10} {'Type':<8} Description")
    print("-" * 70)

    for t in filtered:
        # Convert string date to datetime object
        date_obj = datetime.strptime(t['date'], "%Y-%m-%d")
        formatted_date = date_obj.strftime("%b %d, %Y")

        print(f"{t['transaction_id']:<5} {formatted_date:<15} {t['customer_id']:<12} "
              f"{t['amount']:<10.2f} {t['type']:<8} {t['description']}")

    print(f"\nTotal transactions shown: {len(filtered)}\n")


if __name__ == '__main__':
    transactions = []

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
            print("Invalid option. Try again.\n")

# changes date_obj = datetime.strptime(t['date'], "%Y-%m-%d")
# formatted_date = date_obj.strftime("%b %d, %Y")
# print(f"{t['transaction_id']:<5} {formatted_date:<15} {t['customer_id']:<12} "
#      f"{t['amount']:<10.2f} {t['type']:<8} {t['description']}")
