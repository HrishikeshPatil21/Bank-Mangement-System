# account.py
# This file defines the Account class.
# An Account object simply stores the details of one bank account.

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    # Converts the account details into one line of text
    # so it can be saved in the accounts.txt file.
    # Format: account_number|name|balance
    def to_line(self):
        return f"{self.account_number}|{self.name}|{self.balance}\n"
