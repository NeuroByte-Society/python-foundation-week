class BankAccount:
    def __init__(self, owner, password, balance=0):
        self.owner = owner
        self.__password = password  # Private
        self._balance = balance     # Protected

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount, password):
        if password != self.__password:
            print("Incorrect password!")
            return
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
        else:
            print("Insufficient funds!")

    def get_balance(self, password):
        if password == self.__password:
            return self._balance
        else:
            print("Incorrect password!")
            return None

# Test
account = BankAccount("Alice", "1234", 5000)
account.deposit(2000)
print(account.get_balance("1234"))
account.withdraw(1000, "1234")
account.withdraw(200, "wrong")
