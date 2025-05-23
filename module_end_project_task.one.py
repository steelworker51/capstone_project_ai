import csv
from datetime import datetime

def load_transactions(filename='financial_transactions.csv'):
    transactions = []

    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    date = datetime.strptime(row['date'], '%Y-%m-%d')

                    amount = float(row['amount'])
                    if row['type'].lower() == 'debit':
                        amount = -amount

                    transaction = {
                        'date': date,
                        'description': row['description'],
                        'amount': amount,
                        'type': row['type'].lower()
                    }
                    transactions.append(transaction)
                except ValueError as ve:
                    print(f"Skipping row due to value error: {ve}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    return transactions

# === Call the function and print results ===
if __name__ == '__main__':
    print("Loading transactions...")
    transactions = load_transactions()
    print(f"Loaded {len(transactions)} transactions.\n")

    for tx in transactions:
        print(f"{tx['date'].strftime('%Y-%m-%d')} | {tx['description']} | {tx['amount']} | {tx['type']}")
