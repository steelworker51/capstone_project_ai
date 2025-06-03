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

def generate_report(transactions):
    if not transactions:
        print("No transactions to report")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d")
    filename = f"report_{timestamp}.txt"

    dates = [datetime.strptime(t['date'], "%Y-%m-%d") for t in transactions]
    start_date = min(dates).strftime("%Y-%m-%d")
    end_date = max(dates).strftime("%Y-%m-%d")

    total = sum(t['amount'] for t in transactions)
    debit = sum(t['amount'] for t in transactions if t['type'] == 'debit')
    credit = sum(t['amount'] for t in transactions if t['type'] == 'credit')
    num = len(transactions)

    report = (
        "--- Financial Summary Report ---\n"
        f"Date Range: {start_date} to {end_date}\n"
        f"Total Transactions: {num}\n"
        f"Total Amount: ${total:.2f}\n"
        f"  Debit Total: ${debit:.2f}\n"
        f"  Credit Total: ${credit:.2f}\n"
    )

    try: 
        with open(filename, "w") as f:
            f.write(report)
        print(f"Report generated and saved to {filename}.\n")
    except Exception as e:
        print(f"Error generating report: {e}")

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
        print("3. Print report and include transaction date range")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_transaction(transactions)
        elif choice == '2':
            view_transactions(transactions)
        elif choice == '3':
            generate_report(transactions)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")