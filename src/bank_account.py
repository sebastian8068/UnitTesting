from datetime import datetime
from src.exceptions import (
    WithdrawalTimeRestrictionError,
    WithdrawalWeekEndRestrictionError,
)


class BankAccount:
    def __init__(self, name: str, balance: float = 0, log_file=None) -> None:
        self.balance = balance
        self.log_file = log_file
        self._log_transaction("cuenta creada")
        self.name = name

    def _log_transaction(self, message: str) -> None:
        if self.log_file:
            with open(self.log_file, "a") as file:
                file.write(f"{message}\n")

    def deposit(self, amount: float) -> float:
        if amount > 0:
            self.balance += amount
            self._log_transaction(
                f"deposited {amount}. New balance: {self.balance}"
            )
        else:
            raise ValueError("The amount can't be less than 0")
        return self.balance

    def withdraw(self, amount: float) -> float:
        now = datetime.now()
        if now.hour < 8 or now.hour > 17:
            raise WithdrawalTimeRestrictionError(
                "Withdrawal are only allowed from 8am to 5pm"
            )

        currentDatetime = datetime.today()
        currentWeekDay = currentDatetime.weekday()
        if currentWeekDay in (6, 5):
            raise WithdrawalWeekEndRestrictionError(
                "Withdrawal are only allowed from monday to friday"
            )

        if amount > 0:
            self.balance -= amount
            self._log_transaction(
                f"Withdrew {amount}. New balance: {self.balance}"
            )
        return self.balance

    def get_balance(self) -> float:
        self._log_transaction(
            f"Checked balance. Current balance {self.balance}"
        )
        return self.balance

    def transfer(self, beneficiary, amount: float) -> float:
        if self.balance > amount:
            beneficiary.deposit(amount)
            self.withdraw(amount)
            self._log_transaction(
                f"{self.name} deposited {amount} to {beneficiary.name}, Current balance {self.balance}"
            )
            return self.get_balance()
        else:
            self._log_transaction(
                f"insufficient funds: {self.balance} is more than {amount}"
            )
            raise ValueError("insufficient funds")
