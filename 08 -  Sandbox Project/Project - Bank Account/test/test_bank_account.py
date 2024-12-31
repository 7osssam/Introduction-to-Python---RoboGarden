import unittest
from src.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("John Doe", "savings", 1000)

    def test_create_account(self):
        self.assertEqual(self.account.name, "John Doe")
        self.assertEqual(self.account.accountType, "savings")
        self.assertEqual(self.account.balance, 1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.get_balance(), 800)

    def test_withdraw_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_get_account_number(self):
        self.assertIsNotNone(self.account.get_account_number())

    def test_get_holder_name(self):
        self.assertEqual(self.account.get_holder_name(), "John Doe")

    def test_get_account_type(self):
        self.assertEqual(self.account.get_account_type(), "savings")
        
    def test_transaction_history(self):
        self.account.deposit(500)
        self.account.withdraw(200)
        history = [line.strip() for line in self.account.get_transaction_history()]
        self.assertIn("Deposited: $500", history)
        self.assertIn("Withdrew: $200", history)
        
	# tests clean up
    def tearDown(self):
        del self.account
    # removing any *_transactions.txt file 
        import os
        for file in os.listdir():
           if file.endswith("_transactions.txt"):
               os.remove(file)



if __name__ == "__main__":
    unittest.main()