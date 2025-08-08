# Day 9: Classes and Objects

## 📘 Topics

### 1. Class
- A **class** is a blueprint for creating objects.
- Defines how objects will look and behave.

Example:
```python
class Student:
    pass
```

---

### 2. `__init__()` Constructor
- Special method called automatically when creating an object.
- Used to initialize attributes.

Example:
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

### 3. `self`
- Refers to the **current object**.
- Used to access attributes and methods of the object.

Example:
```python
def show(self):
    print(self.name)
```

---

### 4. Creating Objects
```python
student1 = Student("Alex", 18)
student2 = Student("Maria", 20)
```

---

### 5. Attributes & Methods
- **Attributes**: Variables in a class (e.g., `name`, `age`)
- **Methods**: Functions in a class (e.g., `show_profile()`, `deposit()`)

Example:
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I’m {self.name} and I’m {self.age} years old.")
```

---

## 🛠️ Projects
### 1. Student Record Class
### 2. Rectangle Class
### 3. Simple Bank Account

---

## 🔁 Summary Table

| Concept       | Meaning |
|--------------|---------|
| `class`       | Blueprint for objects |
| `__init__()`  | Constructor method |
| `self`        | Refers to current object |
| Object        | Instance of a class |
| Attributes    | Variables inside a class |
| Methods       | Functions inside a class |
