import os
import unittest
from src.bank_account import BankAccount
from unittest.mock import patch
from src.exceptions import (
    WithdrawalTimeRestrictionError,
    WithdrawalWeekEndRestrictionError,
)


class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(
            name="Luis", balance=1000, log_file="transaction_log.txt"
        )

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename) -> int:
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit_positive_amount_increase_balance(self):
        new_balance = self.account.deposit(500)
        # assert new_balance == 1500
        self.assertEqual(new_balance, 1500, "The balance is not equal")

    def test_deposit_negative_amount_value_error(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    @patch("src.bank_account.datetime")
    def test_withdraw_positive_amount_decrease_balance(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8
        new_balance = self.account.withdraw(200)
        # assert new_balance == 800
        self.assertEqual(new_balance, 800, "The balance is not equal")

    def test_get_balance_returns_correct_value(self):
        balance = self.account.get_balance()
        # assert balance == 1000
        self.assertEqual(balance, 1000, "The balance is not equal")

    @patch("src.bank_account.datetime")
    def test_transfer_positive_amount_updates_both_balances(
        self, mock_datetime
    ):
        mock_datetime.now.return_value.hour = 8
        user1 = BankAccount(name="Pedro", balance=1000)
        user2 = self.account.transfer(user1, 300)
        # print(user1)

        # assert user1.get_balance() == 1300
        # assert user2 == 700
        self.assertEqual(user1.get_balance(), 1300, "The balance is not equal")
        self.assertEqual(user2, 700, "The balance is not equal")

    def test_log_transaction_creates_file_after_deposit(self):
        self.account.deposit(500)
        # assert os.path.exists("transaction_log.txt")
        self.assertTrue(
            os.path.exists("transaction_log.txt"), "The file does not exist"
        )

    def test_count_transaction_increments_with_each_operation(self):
        file_path: int = self.account.log_file
        # assert self._count_lines(self.account.log_file) == 1
        self.assertEqual(
            self._count_lines(file_path), 1, "The line count is not equal"
        )
        self.account.deposit(500)
        # assert self._count_lines(self.account.log_file) == 2
        self.assertEqual(
            self._count_lines(file_path), 2, "The line count is not equal"
        )

        with self.assertRaises(ValueError):
            beneficiary = BankAccount(name="Luis")
            self.account.transfer(beneficiary, 1500)
        # assert self._count_lines(self.account.log_file) == 3
        self.assertEqual(
            self._count_lines(file_path), 3, "The line count is not equal"
        )

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_before_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_after_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 19
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_during_working_days(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        mock_datetime.today.return_value.weekday.return_value = 2
        new_balance = self.account.withdraw(10)
        self.assertEqual(new_balance, 990)

    @patch("src.bank_account.datetime")
    def test_withdraw_on_saturday_WithdrawalWeekEndRestrictionError(
        self, mock_datetime
    ):
        mock_datetime.now.return_value.hour = 10
        mock_datetime.today.return_value.weekday.return_value = 5
        with self.assertRaises(WithdrawalWeekEndRestrictionError):
            self.account.withdraw(10)

    @patch("src.bank_account.datetime")
    def test_withdraw_on_sunday_WithdrawalWeekEndRestrictionError(
        self, mock_datetime
    ):
        mock_datetime.now.return_value.hour = 10
        mock_datetime.today.return_value.weekday.return_value = 6
        with self.assertRaises(WithdrawalWeekEndRestrictionError):
            self.account.withdraw(10)

    def test_deposit_multiples_values(self):
        test_cases = [
            {"amount": 100, "expected": 1100},
            {"amount": 3000, "expected": 4000},
            {"amount": 4500, "expected": 5500},
        ]

        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(
                    balance=1000, log_file="transaction_log.txt", name="jhon"
                )

                new_balance = self.account.deposit(case["amount"])
                self.assertEqual(new_balance, case["expected"])
