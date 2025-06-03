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

def modify_transaction(transactions):
    """Modify an existing transaction by ID."""
    if not transactions:
        print("No transactions to modify.")
        return
    
    print("\n--- Modify Transaction ---")
    # List transactions briefly
    for t in transactions:
        print(f"ID {t['transaction_id']}: {t['description']} on {t['date']} (${t['amount']:.2f})")

    user_input = input("Enter the transaction ID to modify (or 'cancel' to abort): ")
    if user_input.lower() == 'cancel':
        print("Modification cancelled.")
        return

    try:
        tid = int(user_input)
    except ValueError:
        print("Invalid ID format.")
        return

    # Find transaction by ID
    transaction = next((t for t in transactions if t['transaction_id'] == tid), None)
    if not transaction:
        print(f"No transaction found with ID {tid}.")
        return

    print(f"Selected transaction: {transaction}")

    # Fields user can modify
    fields = ['date', 'customer_id', 'amount', 'type', 'description']
    print("Fields available to modify:", ', '.join(fields))

    field = input("Enter field to modify(or cancel to abort): ").lower()
    if field == 'cancel':
        print("Modification cancelled.")
        return
    if field not in fields:
        print("Invalid field.")
        return

    new_value = input(f"Enter new value for {field} (or 'cancel to abort): ")
    if new_value.lower() == 'cancel':
        print("Modification cancelled.")
        return
    
    # Validate inputs depending on field
    if field == 'date':
        try:
            datetime.strptime(new_value, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format, must be YYYY-MM-DD.")
            return
    elif field == 'amount':
        try:
            new_value = float(new_value)
        except ValueError:
            print("Amount must be a number.")
            return
    elif field == 'type':
        if new_value.lower() not in ['debit', 'credit']:
            print("Type must be 'debit' or 'credit'.")
            return
        new_value = new_value.lower()

    # Apply the modification
    transaction[field] = new_value
    print("Transaction updated successfully.")


def remove_transaction(transactions):
    """Remove a transaction by ID."""
    if not transactions:
        print("No transactions to remove.")
        return

    print("\n--- Remove Transaction ---")
    for t in transactions:
        print(f"ID {t['transaction_id']}: {t['description']} on {t['date']} (${t['amount']:.2f})")

    user_input = input("Enter the transaction ID to remove (or 'cancel' to abort): ")
    if user_input.lower() == 'cancel':
        print("Removal cancelled.")
        return


    try:
        tid = int(user_input)
    except ValueError:
        print("Invalid ID format.")
        return

    # Find index to remove
    index = next((i for i, t in enumerate(transactions) if t['transaction_id'] == tid), None)
    if index is None:
        print(f"No transaction found with ID {tid}.")
        return

    removed = transactions.pop(index)
    print(f"Transaction ID {removed['transaction_id']} removed.")

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
        print("\nMenu:")
        print("1. View Transactions")
        print("2. Add Transaction")
        print("3. Modify Transaction")
        print("4. Remove Transaction")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            view_transactions(transactions)
        elif choice == '2':
            add_transaction(transactions)
        elif choice == '3':
            modify_transaction(transactions)
        elif choice == '4':
            remove_transaction(transactions)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# lines 81-90 gives the option to cancel in the modify transaction block
# use the user_input directly
# lines 145-148 gives the option to cancel in the remove transaction block
# when choosing modify option theree it give you the option enter the transaction id to modify or you can type cancel to abort
# 158 it again uses user_input directly