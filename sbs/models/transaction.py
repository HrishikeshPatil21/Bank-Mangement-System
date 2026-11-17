# transaction.py
# This file defines the Transaction class.
# A Transaction object stores the details of ONE transaction
# (deposit, withdrawal, transfer, or account creation).
#
# Date and Time are captured automatically using Python's
# built-in datetime module, and stored as TWO separate fields.

from datetime import datetime

class Transaction:
    def __init__(self, account_number, txn_type, amount, prev_balance, new_balance):
        now = datetime.now()
        self.date = now.strftime("%d-%m-%Y")   # e.g. 07-08-2026
        self.time = now.strftime("%I:%M %p")   # e.g. 07:02 AM

        self.account_number = account_number
        self.txn_type = txn_type
        self.amount = amount
        self.prev_balance = prev_balance
        self.new_balance = new_balance

    # Converts the transaction details into one line of text
    # so it can be saved in the transactions.txt file.
    # Format: date|time|account_number|txn_type|amount|prev_balance|new_balance
    def to_line(self):
        return f"{self.date}|{self.time}|{self.account_number}|{self.txn_type}|{self.amount}|{self.prev_balance}|{self.new_balance}\n"