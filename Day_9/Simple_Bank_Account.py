class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Insufficient funds!")

    def check_balance(self):
        print(f"Account Balance: ₹{self.balance}")

acc = BankAccount("John", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.check_balance()
