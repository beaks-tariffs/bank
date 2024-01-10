# transaction.py

class Transaction:
    @staticmethod
    def perform_transaction(account, amount):
        print(f"Performing transaction on account {account.account_number}:")
        account.deposit(amount)
        account.withdraw(amount / 2)
        account.display()
