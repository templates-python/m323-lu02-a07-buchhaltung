"""Buchhaltung.

Aufgabenstellung: https://wiki.bzz.ch/modul/m323/learningunits/lu02/aufgaben/buchhaltung
"""

def add_transaction(transactions, new_transaction):
    """
    Adds a new transaction to the existing list of transactions.

    Parameters:
        transactions (tuple): The existing list of transactions.
        new_transaction (tuple): The new transaction to be added.

    Returns:
        tuple: A new list of transactions including the new transaction.
    """
    return transactions + (new_transaction,)


def calculate_balance(transactions):
    """
    Calculates the current balance based on the list of transactions.

    Parameters:
        transactions (tuple): The list of transactions.

    Returns:
        float: The current balance.
    """
    balance = 0
    for transaction in transactions:
        transaction_type, amount = transaction
        if transaction_type == 'Deposit':
            balance += amount
        elif transaction_type == 'Withdrawal':
            balance -= amount
    return balance


if __name__ == '__main__':
    # Beispiel für die Datenstruktur der Transaktionen
    demo_transactions = (('Deposit', 1000), ('Withdrawal', 200))
    # Füge eine neue Transaktion hinzu
    demo_transactions = add_transaction(demo_transactions, ('Deposit', 500))
    demo_transactions = add_transaction(demo_transactions, ('Withdrawal', 100))
    demo_transactions = add_transaction(demo_transactions, ('Deposit', 300))
    # Berechne den aktuellen Kontostand
    demo_balance = calculate_balance(demo_transactions)
    print(f'Transaktionen: {demo_transactions}, Kontostand {demo_balance}')
