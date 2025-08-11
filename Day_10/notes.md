# ✅ Day 10: Inheritance + Encapsulation

## 📘 Topics


### 1. Inheritance
Inheritance allows a class (child/subclass) to acquire properties and methods from another class (parent/superclass).

**Key points:**
- Use `class Child(Parent)` to inherit.
- Use `super()` to call the parent class's methods/attributes.
- Promotes **code reusability**.

**Example:**
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        super().speak()  # Call parent method
        print(f"{self.name} barks.")

dog = Dog("Buddy")
dog.speak()
````

---

### 2. Encapsulation

Encapsulation is the practice of restricting direct access to an object’s attributes and methods to protect the data.

**Key points:**

* **Protected attributes**: `_attr` → By convention, should not be accessed outside the class.
* **Private attributes**: `__attr` → Name-mangled to prevent direct access from outside.
* Use **getter** and **setter** methods to control access.

**Example:**

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # Protected

    def deposit(self, amount):
        self._balance += amount
    
    def get_balance(self):
        return self._balance

account = BankAccount("Alice", 5000)
account.deposit(2000)
print(account.get_balance())  # 7000
```

---

## 🛠️ Projects

1. **Animal → Dog/Cat Inheritance Example**

   * Create a base `Animal` class.
   * Add `Dog` and `Cat` subclasses.
   * Override the `speak()` method in each subclass.

2. **Secure Bank System**

   * `_balance` as a protected attribute.
   * Methods: `deposit()`, `withdraw()`.
   * Withdraw requires password verification.

3. **Employee Payroll System**

   * Base `Employee` class with `name`, `salary`.
   * `Manager` subclass adds `bonus` and overrides a method to calculate total pay.

---

## 💡 Summary

* **Inheritance** → Reuse and extend existing classes.
* **Encapsulation** → Hide internal details and control access to attributes.
* Combine both for **clean, secure, and maintainable code**.

