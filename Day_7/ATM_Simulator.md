### 🔹 1. ATM Simulator

```python
balance = 1000

def check_balance():
    print("💰 Balance:", balance)

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("✅ Withdrawn:", amount)
    else:
        print("❌ Insufficient funds.")

def deposit(amount):
    global balance
    balance += amount
    print("✅ Deposited:", amount)

# Menu
while True:
    print("\n--- ATM ---")
    print("1. Check Balance\n2. Withdraw\n3. Deposit\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        amt = int(input("Enter amount: "))
        withdraw(amt)
    elif choice == "3":
        amt = int(input("Enter amount: "))
        deposit(amt)
    elif choice == "4":
        print("👋 Bye!")
        break
    else:
        print("⚠️ Invalid option")

```

✅ Demonstrates functions + conditions + user input.
