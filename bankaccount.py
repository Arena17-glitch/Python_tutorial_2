""" Moderate Problem: Bank Account Management System
Problem Statement:
Design a class BankAccount with:
Class Attributes:
• bank_name = "National Bank"
• total_accounts = 0
• total_bank_balance = 0
Instance Attributes:
• account_holder
• balance
Requirements:
• Increment total_accounts when a new account is created.
• Add the initial deposit to total_bank_balance.
• Create methods:
• deposit(amount) → increase balance and update:total_bank_balance
• withdraw(amount) → decrease balance and update total_bank_balance
• display_account_info()
• Ensure withdrawal cannot exceed balance.
• Add a class method display_bank_summary() that prints:
• Bank name
• Total accounts
• Total bank balance
"""

class BankAccount:
    bank_name = "National Bank"
    total_accounts = 0
    total_bank_balance = 0

    def __init__(self, account_holder, initial_deposit):
        self.account_holder = account_holder
        self.balance = initial_deposit

        BankAccount.total_accounts += 1
        BankAccount.total_bank_balance += initial_deposit
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            BankAccount.total_bank_balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance. Withdrawal denied.")
        else:
            self.balance -= amount
            BankAccount.total_bank_balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.balance}")

    def display_account_info(self):
        print("----- Account Information -----")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")
        print("--------------------------------")

    @classmethod
    def display_bank_summary(cls):
        print("===== Bank Summary =====")
        print(f"Bank Name: {cls.bank_name}")
        print(f"Total Accounts: {cls.total_accounts}")
        print(f"Total Bank Balance: {cls.total_bank_balance}")
        print("========================")
        

acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 2000)

acc1.deposit(500)
acc2.withdraw(1000)

acc1.display_account_info()
acc2.display_account_info()

BankAccount.display_bank_summary()