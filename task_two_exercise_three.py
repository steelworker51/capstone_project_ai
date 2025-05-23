from datetime import datetime

def add_transaction(transactions):
    """Add a new transaction from user input, with customer ID suggestions."""
    print("\n--- Add New Transaction ---")

    # ✅ Suggest existing customer IDs
    existing_ids = set(t['customer_id'] for t in transactions)
    if existing_ids:
        print(f"Existing customer IDs: {', '.join(sorted(existing_ids))}")
    else:
        print("No customer IDs yet — you will create the first one.")

    # Date input
    while True:
        date_input = input("Enter date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_input, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    # Customer ID input
    customer_id = input("Enter customer ID: ")

    # Amount input
    while True:
        amount_input = input("Enter amount: ")
        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("Amount must be a number.")

    # Type input
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

    # Create transaction
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

# this code will check and see if a customer id has already created, if there is not record it will display "no customer ids yet-you will create the first one"
# but upon creating a customer id or if you have some available it wil suggest existing customer id's