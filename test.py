class BankAccount:
    def __init__(self, account_holder, initial_balance):
        # Private attribute (not directly accessible from outside)
        self.__balance = initial_balance
        self.account_holder = account_holder

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount=0):
        """Withdraw money from the account."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return f"{self.__balance} Remaining"

account = BankAccount("John Doe", 100)
account.deposit(50)
account.withdraw(10)
print(account.get_balance())
print(account.withdraw(100))