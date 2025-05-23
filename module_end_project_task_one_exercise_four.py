import csv
from datetime import datetime

def load_transactions(filename='financial_transaction.csv', error_log='errors.txt'):
    transactions = []
    skipped_rows = []

    # Open the error log file in write mode (overwrites each time)
    with open(error_log, 'w') as log_file:
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row_num, row in enumerate(reader, start=2):  # start=2 to match CSV line numbers
                    try:
                        # Validate and parse date
                        date = datetime.strptime(row['date'], '%Y-%m-%d')

                        # Validate and parse amount
                        try:
                            amount = float(row['amount'])
                        except ValueError:
                            message = f"Row {row_num}: Invalid amount '{row['amount']}'"
                            skipped_rows.append((row_num, message))
                            log_file.write(message + '\n')
                            continue

                        # Validate type (optional strict check)
                        if row['type'].lower() not in ['debit', 'credit']:
                            message = f"Row {row_num}: Invalid type '{row['type']}'"
                            skipped_rows.append((row_num, message))
                            log_file.write(message + '\n')
                            continue

                        # Make amount negative if it's a debit
                        if row['type'].lower() == 'debit':
                            amount = -amount

                        # Store valid transaction
                        transaction = {
                            'date': date,
                            'description': row['description'],
                            'amount': amount,
                            'type': row['type'].lower()
                        }
                        transactions.append(transaction)

                    except ValueError as ve:
                        message = f"Row {row_num}: Value error - {ve}"
                        skipped_rows.append((row_num, message))
                        log_file.write(message + '\n')

        except FileNotFoundError:
            log_file.write(f"Error: The file '{filename}' was not found.\n")
            print(f"Error: The file '{filename}' was not found.")

    return transactions, skipped_rows

if __name__ == '__main__':
    transactions, skipped_rows = load_transactions()
    print(f"Loaded {len(transactions)} valid transactions.")

    if skipped_rows:
        print("\nSkipped rows due to errors (see errors.txt):")
        for row_num, message in skipped_rows:
            print(f" - {message}")
    else:
        print("No rows were skipped.")
