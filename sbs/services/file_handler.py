# file_handler.py
# This file contains simple functions to read from and write to
# our two data files: accounts.txt and transactions.txt
# This is where "File Handling" actually happens in the project.

ACCOUNTS_FILE = "data/accounts.txt"
TRANSACTIONS_FILE = "data/transactions.txt"


# Reads all accounts from accounts.txt
# Returns a list of lines, where each line is one account record.
def read_accounts():
    with open(ACCOUNTS_FILE, "r") as file:
        lines = file.readlines()
    return lines


# Adds ONE new account to accounts.txt (used when creating an account)
def add_account_to_file(account):
    with open(ACCOUNTS_FILE, "a") as file:
        file.write(account.to_line())


# Rewrites the entire accounts.txt file with updated balances.
# We use this every time a balance changes (deposit/withdraw/transfer).
def update_accounts_file(all_lines):
    with open(ACCOUNTS_FILE, "w") as file:
        file.writelines(all_lines)


# Adds ONE new transaction record to transactions.txt
def add_transaction_to_file(transaction):
    with open(TRANSACTIONS_FILE, "a") as file:
        file.write(transaction.to_line())


# Reads all transactions belonging to one particular account number
# Each returned record is a list:
# [date, time, account_number, txn_type, amount, prev_balance, new_balance]
def read_transactions_for_account(account_number):
    matching_lines = []
    with open(TRANSACTIONS_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue  # skip blank lines

            parts = line.split("|")
            if len(parts) != 7:
                continue  # skip old-format or broken lines

            if parts[2] == account_number:
                matching_lines.append(parts)
    return matching_lines