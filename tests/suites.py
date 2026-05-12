import unittest
from test_bank_account import BankAccountTests


def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(
        BankAccountTests("test_deposit_positive_amount_increase_balance")
    )
    suite.addTest(BankAccountTests("test_deposit_negative_amount_value_error"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())
