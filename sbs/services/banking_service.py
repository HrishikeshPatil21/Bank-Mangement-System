# banking_service.py
# This file contains all the main banking operations:
# create account, deposit, withdraw, transfer, check balance,
# view history, and search account.
#
# Each function reads the accounts.txt file when it needs the
# latest data, and writes back to it whenever something changes.
# This keeps the logic easy to follow, step by step.

from models.account import Account
from models.transaction import Transaction
from services import file_handler


# Finds one account by account number.
# Returns an Account object if found, otherwise None.
def find_account(account_number):
    lines = file_handler.read_accounts()
    for line in lines:
        parts = line.strip().split("|")
        if parts[0] == account_number:
            return Account(parts[0], parts[1], float(parts[2]))
    return None


# Generates the next account number by looking at existing accounts.
# First account starts at 1001.
def generate_account_number():
    lines = file_handler.read_accounts()
    if len(lines) == 0:
        return "1001"
    last_line = lines[-1]
    last_number = int(last_line.strip().split("|")[0])
    return str(last_number + 1)


# 1. CREATE ACCOUNT
def create_account(name, initial_deposit):
    account_number = generate_account_number()
    account = Account(account_number, name, initial_deposit)
    file_handler.add_account_to_file(account)

    txn = Transaction(account_number, "Account Created", initial_deposit, 0, initial_deposit)
    file_handler.add_transaction_to_file(txn)

    return account_number


# 2. DEPOSIT MONEY
def deposit(account_number, amount):
    lines = file_handler.read_accounts()
    updated_lines = []
    new_balance = None
    old_balance = None

    for line in lines:
        parts = line.strip().split("|")
        if parts[0] == account_number:
            old_balance = float(parts[2])
            new_balance = old_balance + amount
            parts[2] = str(new_balance)
            updated_lines.append("|".join(parts) + "\n")
        else:
            updated_lines.append(line)

    if new_balance is None:
        return None  # account not found

    file_handler.update_accounts_file(updated_lines)
    txn = Transaction(account_number, "Deposit", amount, old_balance, new_balance)
    file_handler.add_transaction_to_file(txn)
    return new_balance


# 3. WITHDRAW MONEY
def withdraw(account_number, amount):
    lines = file_handler.read_accounts()
    updated_lines = []
    new_balance = None
    old_balance = None

    for line in lines:
        parts = line.strip().split("|")
        if parts[0] == account_number:
            old_balance = float(parts[2])
            if amount > old_balance:
                return "INSUFFICIENT_BALANCE"
            new_balance = old_balance - amount
            parts[2] = str(new_balance)
            updated_lines.append("|".join(parts) + "\n")
        else:
            updated_lines.append(line)

    if new_balance is None:
        return None  # account not found

    file_handler.update_accounts_file(updated_lines)
    txn = Transaction(account_number, "Withdrawal", amount, old_balance, new_balance)
    file_handler.add_transaction_to_file(txn)
    return new_balance


# 4. TRANSFER MONEY (from one account to another)
def transfer(from_number, to_number, amount):
    lines = file_handler.read_accounts()
    updated_lines = []

    from_old = from_new = to_old = to_new = None
    from_found = to_found = False

    for line in lines:
        parts = line.strip().split("|")
        if parts[0] == from_number:
            from_found = True
            from_old = float(parts[2])
            if amount > from_old:
                return "INSUFFICIENT_BALANCE"
            from_new = from_old - amount
            parts[2] = str(from_new)
        elif parts[0] == to_number:
            to_found = True
            to_old = float(parts[2])
            to_new = to_old + amount
            parts[2] = str(to_new)
        updated_lines.append("|".join(parts) + "\n")

    if not from_found or not to_found:
        return None  # one or both accounts not found

    file_handler.update_accounts_file(updated_lines)

    txn1 = Transaction(from_number, f"Transfer to {to_number}", amount, from_old, from_new)
    txn2 = Transaction(to_number, f"Transfer from {from_number}", amount, to_old, to_new)
    file_handler.add_transaction_to_file(txn1)
    file_handler.add_transaction_to_file(txn2)

    return from_new


# 5. CHECK BALANCE
def check_balance(account_number):
    account = find_account(account_number)
    if account is None:
        return None
    return account.balance


# 6. VIEW TRANSACTION HISTORY
def view_history(account_number):
    return file_handler.read_transactions_for_account(account_number)


# 7. SEARCH ACCOUNT
def search_account(account_number):
    return find_account(account_number)