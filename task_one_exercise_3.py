import csv
from datetime import datetime

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
                        skipped_rows.append((row_num, f"Invalid amount: {row['amount']}"))
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
                    skipped_rows.append((row_num, f"Value error: {ve}"))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

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