# Bank Account Simulation

## Overview
This project is a Python-based simulation of a bank account system. It supports creating accounts, managing transactions, and maintaining a record of transaction history using file storage. The simulation includes functionalities for deposit, withdrawal, and balance checks, with transaction details saved to files for persistence.

## Features
- **Account Management:** Create accounts with unique account numbers.
- **Transaction Management:**
  - Deposit money.
  - Withdraw money.
  - Check balance.
  - View transaction history.
- **Transaction Persistence:** All transactions are saved to text files named based on the account number and type.
- **Command-Line Interface:** A user-friendly CLI to interact with the system.
- **Unit Testing:** Comprehensive tests to validate the functionality.

## Folder Structure
```
.
|-- src
|   |-- __init__.py
|   |-- bank_account.py       # Core bank account logic
|   |-- main.py               # CLI entry point
|   `-- utils
|       `-- __init__.py
|-- test
|   |-- __init__.py
|   |-- test_bank_account.py  # Unit tests for bank account
|-- README.md                 # Project documentation
|-- requirements.txt          # Python dependencies
```

## Installation

### Prerequisites
- Python 3.8+

### Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd bank-account-simulation
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run tests to ensure everything is working:
   ```bash
   python -m unittest discover test
   ```
4. Start the application:
   ```bash
   python src/main.py
   ```

## Usage
1. **Run the CLI:**
   ```bash
   python src/main.py
   ```
2. Choose options from the menu to perform actions like creating an account, depositing money, or checking transaction history.

## Unit Testing
The project includes unit tests to validate the functionality of the bank account system. Run the tests with:
```bash
python -m unittest discover test
```

## Key Classes
### `BankAccount`
This class represents a bank account and includes methods for:
- Creating and managing account details.
- Depositing and withdrawing funds.
- Fetching and logging transaction history.

#### Methods
- `__init__(name, accountType, balance)` - Initialize the account.
- `deposit(amount)` - Deposit funds.
- `withdraw(amount)` - Withdraw funds.
- `get_balance()` - Check the current balance.
- `get_transaction_history()` - Retrieve the transaction history.
- `log_transaction(transaction)` - Log a transaction.

### `main.py`
The entry point for the CLI interface.

## Example
### Sample Interaction
```plaintext
============== Bank Account Simulation =================
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Transaction History
6. Exit
=========================================================
Enter your choice: 1
Enter account holder name: John Doe
Enter account type (savings/chequing): savings
Enter initial balance: 1000
Account created successfully! Account Number: 123456
```


## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
Developed as part of a Introduction to Python - RoboGarden Upskilling course.
