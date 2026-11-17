# main.py
# This is the starting point of the program.
# It shows a menu to the user and calls the correct function
# from banking_service.py based on the user's choice.

from services import banking_service


def show_menu():
    print("\n===== BANKING SYSTEM MENU =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. View Transaction History")
    print("7. Search Account")
    print("8. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ")

        # 1. CREATE ACCOUNT
        if choice == "1":
            name = input("Enter your name: ")
            amount = float(input("Enter initial deposit amount: "))
            account_number = banking_service.create_account(name, amount)
            print("Account created successfully! Your account number is:", account_number)

        # 2. DEPOSIT
        elif choice == "2":
            acc_no = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            result = banking_service.deposit(acc_no, amount)
            if result is None:
                print("Account not found.")
            else:
                print("Deposit successful! New balance:", result)

        # 3. WITHDRAW
        elif choice == "3":
            acc_no = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            result = banking_service.withdraw(acc_no, amount)
            if result is None:
                print("Account not found.")
            elif result == "INSUFFICIENT_BALANCE":
                print("Insufficient balance!")
            else:
                print("Withdrawal successful! New balance:", result)

        # 4. TRANSFER
        elif choice == "4":
            from_acc = input("Enter your account number: ")
            to_acc = input("Enter recipient's account number: ")
            amount = float(input("Enter amount to transfer: "))
            result = banking_service.transfer(from_acc, to_acc, amount)
            if result is None:
                print("One or both account numbers are invalid.")
            elif result == "INSUFFICIENT_BALANCE":
                print("Insufficient balance!")
            else:
                print("Transfer successful! Your new balance:", result)

        # 5. CHECK BALANCE
        elif choice == "5":
            acc_no = input("Enter account number: ")
            balance = banking_service.check_balance(acc_no)
            if balance is None:
                print("Account not found.")
            else:
                print("Current balance:", balance)

        # 6. VIEW TRANSACTION HISTORY
        elif choice == "6":
            acc_no = input("Enter account number: ")
            history = banking_service.view_history(acc_no)
            if len(history) == 0:
                print("No transactions found for this account.")
            else:
                print("\n----- TRANSACTION HISTORY -----")
                for record in history:
                    date, time, acc, txn_type, amount, prev_bal, new_bal = record
                    print("Date            :", date)
                    print("Time            :", time)
                    print("Transaction Type:", txn_type)
                    print("Amount          :", amount)
                    print("Previous Balance:", prev_bal)
                    print("Current Balance :", new_bal)
                    print("--------------------------------")

        # 7. SEARCH ACCOUNT
        elif choice == "7":
            acc_no = input("Enter account number: ")
            account = banking_service.search_account(acc_no)
            if account is None:
                print("Account not found.")
            else:
                print("Account Number:", account.account_number)
                print("Name          :", account.name)
                print("Balance       :", account.balance)

        # 8. EXIT
        elif choice == "8":
            print("Thank you for using the Banking System!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


# This makes sure main() runs only when this file is run directly.
if __name__ == "__main__":
    main()