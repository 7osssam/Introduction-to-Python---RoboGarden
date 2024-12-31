from bank_account import BankAccount

def main():
    accounts = {}

    while True:
        print("============== Bank Account Simulation =================")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")
        print("=========================================================")
        choice = input("Enter your choice: ")

        if choice == '1':
            holder_name = input("Enter account holder name: ").strip()
            if not holder_name:
                print("Holder name cannot be empty.")
                continue

            while True:
                account_type = input("Enter account type (savings/chequing): ").strip().lower()
                if account_type in ["savings", "chequing"]:
                    break
                elif account_type == "q":
                    print("Exiting...")
                    break
                else:
                    print("Invalid account type. Please try again.")

            try:
                initial_balance = float(input("Enter initial balance: "))
                if initial_balance < 0:
                    print("Initial balance cannot be negative.")
                    continue
            except ValueError:
                print("Invalid input for balance. Please enter a number.")
                continue

            account = BankAccount(holder_name, account_type, initial_balance)
            accounts[account.get_account_number()] = account
            print(f"Account created successfully! Account Number: {account.get_account_number()}")

        elif choice == '2':
            try:
                account_number = int(input("Enter account number: "))
            except ValueError:
                print("Invalid account number. Please enter a valid number.")
                continue

            if account_number in accounts:
                try:
                    amount = float(input("Enter amount to deposit: "))
                    if amount <= 0:
                        print("Deposit amount must be positive.")
                        continue
                except ValueError:
                    print("Invalid input for amount. Please enter a number.")
                    continue

                accounts[account_number].deposit(amount)
                print(f"Deposited ${amount}. New Balance: ${accounts[account_number].get_balance()}")
            else:
                print("Account not found.")

        elif choice == '3':
            try:
                account_number = int(input("Enter account number: "))
            except ValueError:
                print("Invalid account number. Please enter a valid number.")
                continue

            if account_number in accounts:
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    if amount <= 0:
                        print("Withdrawal amount must be positive.")
                        continue
                except ValueError:
                    print("Invalid input for amount. Please enter a number.")
                    continue

                if accounts[account_number].get_balance() < amount:
                    print("Insufficient balance.")
                    continue

                accounts[account_number].withdraw(amount)
                print(f"Withdrew ${amount}. New Balance: ${accounts[account_number].get_balance()}")
            else:
                print("Account not found.")

        elif choice == '4':
            try:
                account_number = int(input("Enter account number: "))
            except ValueError:
                print("Invalid account number. Please enter a valid number.")
                continue

            if account_number in accounts:
                print(f"Balance: ${accounts[account_number].get_balance()}")
            else:
                print("Account not found.")

        elif choice == '5':
            try:
                account_number = int(input("Enter account number: "))
            except ValueError:
                print("Invalid account number. Please enter a valid number.")
                continue

            if account_number in accounts:
                print("Transaction History:")
                for transaction in accounts[account_number].get_transaction_history():
                    print(transaction)
            else:
                print("Account not found.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()