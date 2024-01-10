# banking_system.py

class BankingSystem:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def display_all_accounts(self):
        print("All Accounts in the Banking System:")
        for account in self.accounts:
            account.display()
