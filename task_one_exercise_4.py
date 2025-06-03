import csv
from datetime import datetime

def log_error(message):
    """Log error messages to errors.txt with timestamp."""
    with open("errors.txt", "a") as f:
        f.write(f"{datetime.now().isoformat()} - {message}\n")

def load_transactions(filename='financial_transaction.csv'):
    transactions = []
    skipped_rows = []  # to store info about skipped rows

    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row_num, row in enumerate(reader, start=2):  # start=2 to account for header line
                try:
                    # Parse date
                    date = datetime.strptime(row['date'], '%Y-%m-%d')

                    # Parse amount
                    try:
                        amount = float(row['amount'])
                    except ValueError:
                        error_msg = f"Invalid amout: {row['amount']}"
                        skipped_rows.append((row_num, error_msg))
                        log_error(f"Row {row_num}: {error_msg}")
                        continue

                    # Adjust amount if it's a debit
                    if row['type'].lower() == 'debit':
                        amount = -amount

                    # Build and store transaction
                    transaction = {
                        'date': date,
                        'description': row['description'],
                        'amount': amount,
                        'type': row['type'].lower()
                    }
                    transactions.append(transaction)

                except ValueError as ve:
                    error_msg = f"Value error: {ve}"
                    skipped_rows.append((row_num, error_msg))
                    log_error(f"Row {row_num}: {error_msg}")


    except FileNotFoundError:
        error_msg = f"Error: The file '{filename}' was not found."
        print(error_msg)
        log_error(error_msg)

    return transactions, skipped_rows

# === Main execution block ===
if __name__ == '__main__':
    print("Loading transactions...")
    transactions, skipped_rows = load_transactions()

    print(f"\nLoaded {len(transactions)} valid transactions.")

    # Print skipped row info
    if skipped_rows:
        print("\nSkipped rows due to errors:")
        for row_num, reason in skipped_rows:
            print(f" - Row {row_num}: {reason}")
    else:
        print("\nNo rows were skipped.")

#line 24-28 updated the code in the try except loop to the code to error.txt as well as print out a message for the error in the console
#lines 46-49 updated the outer filenotfounderror blcok to relect the logging of the error message
