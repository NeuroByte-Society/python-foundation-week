class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_total_pay(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_total_pay(self):
        return self.salary + self.bonus

# Test
emp = Employee("John", 50000)
mgr = Manager("Alice", 60000, 15000)

print(f"{emp.name}'s Total Pay: {emp.get_total_pay()}")
print(f"{mgr.name}'s Total Pay: {mgr.get_total_pay()}")
