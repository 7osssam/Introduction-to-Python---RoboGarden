class BankAccount:
    def __init__(self, name, accountType, balance=0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.account_number = self.generate_account_number()
        self.transaction_history = []
        self.create_transaction_file()

    def generate_account_number(self):
        import random
        return random.randint(100000, 999999)

    def create_transaction_file(self):
        with open(f"{self.account_number}_{self.accountType}_transactions.txt", "w") as file:
            file.write("Transaction History:\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.log_transaction(f"Deposited: ${amount}")
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.log_transaction(f"Withdrew: ${amount}")
            else:
                raise ValueError("Insufficient funds.")
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def get_holder_name(self):
        return self.name

    def get_account_type(self):
        return self.accountType

    def get_transaction_history(self):
        with open(f"{self.account_number}_{self.accountType}_transactions.txt", "r") as file:
            return file.readlines()

    def log_transaction(self, transaction):
        import datetime
        self.transaction_history.append(transaction)
        with open(f"{self.account_number}_{self.accountType}_transactions.txt", "a") as file:
            file.write(transaction + "\n")
            file.write(f"{datetime.datetime.now()}\n")
            