# Завдання 3
class BankAccount:
    def __init__(self, owner, account_number, balance=0.0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} UAH deposited. New balance: {self.balance} UAH")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} UAH withdrawn. New balance: {self.balance} UAH")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        print(f"Account balance: {self.balance} UAH")

    def print_account_info(self):
        print(f"BankAccount(owner={self.owner}, account_number={self.account_number}, balance={self.balance})")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner, account_number, initial_balance=0.0):
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            self.accounts[account_number] = BankAccount(owner, account_number, initial_balance)
            print(f"Account for {owner} created successfully.")

    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].balance >= amount and amount > 0:
                self.accounts[from_acc].withdraw(amount)
                self.accounts[to_acc].deposit(amount)
                print(f"Transfer of {amount} UAH from {from_acc} to {to_acc} successful.")
            else:
                print("Insufficient funds or invalid transfer amount.")
        else:
            print("One or both account numbers are invalid.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def list_accounts(self):
        for acc in self.accounts.values():
            acc.print_account_info()


bank = Bank()
bank.create_account("Alice", "12345", 5000)
bank.create_account("Bob", "67890", 3000)

bank.get_account("12345").deposit(1500)
bank.get_account("12345").withdraw(2000)
bank.transfer("12345", "67890", 1000)

bank.list_accounts()
