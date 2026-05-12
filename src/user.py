from src.bank_account import BankAccount


class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.accounts: list[BankAccount] = []

    def add_account(self, account: BankAccount) -> None:
        self.accounts.append(account)

    def get_total_balance(self) -> float:
        return sum(account.get_balance() for account in self.accounts)

