# main.py

from account import Account
from transaction import Transaction
from banking_system import BankingSystem

def main():
    # Create accounts
    account1 = Account(12345, 1000.0)
    account2 = Account(67890, 2000.0)

    # Create a banking system
    banking_system = BankingSystem()

    # Add accounts to the banking system
    banking_system.add_account(account1)
    banking_system.add_account(account2)

    # Perform transactions on accounts
    Transaction.perform_transaction(account1, 500.0)
    Transaction.perform_transaction(account2, 1000.0)

    # Display information about the banking system
    banking_system.display_all_accounts()

if __name__ == "__main__":
    main()
