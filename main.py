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
        type, amount = transaction
        if type == 'Deposit':
            balance += amount
        elif type == 'Withdrawal':
            balance -= amount
    return balance


if __name__ == '__main__':
    # Beispiel für die Datenstruktur der Transaktionen
    transactions = (('Deposit', 1000), ('Withdrawal', 200))
    # Füge eine neue Transaktion hinzu
    transactions = add_transaction(transactions, ('Deposit', 500))
    transactions = add_transaction(transactions, ('Withdrawal', 100))
    transactions = add_transaction(transactions, ('Deposit', 300))
    # Berechne den aktuellen Kontostand
    balance = calculate_balance(transactions)
    print(f'Transaktionen: {transactions}, Kontostand {balance}')
