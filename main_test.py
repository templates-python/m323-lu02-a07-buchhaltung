import main


def test_add_transaction():
    initial_transactions = (('Deposit', 1000), ('Withdrawal', 200))
    new_transaction = ('Deposit', 500)
    updated_transactions = main.add_transaction(initial_transactions, new_transaction)
    assert updated_transactions == (
        ('Deposit', 1000),
        ('Withdrawal', 200),
        ('Deposit', 500),
    )


def test_calculate_balance():
    transactions = (('Deposit', 1000), ('Withdrawal', 200), ('Deposit', 500))
    balance = main.calculate_balance(transactions)
    assert balance == 1300
