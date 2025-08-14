
# ✅ Day 11: Polymorphism + Magic Methods

## 📚 Topics Covered
- **Polymorphism** (Same interface, different behavior)
- **Method Overriding**
- Magic Methods:
  - `__str__`
  - `__len__`
  - `__repr__`
- **Class Methods** vs **Static Methods**

---

## 1️⃣ Polymorphism (Many Forms)

**Definition:**  
Polymorphism allows the **same method name** to behave **differently** depending on the object that calls it.

In other words: *"Same action, different results."*

### Example:
```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())  # Woof!  Meow!

```

🔹 Here, both classes have a `speak()` method, but their implementation is different.

💡 **Why it's useful:**  
You can write **generic code** that works with different object types **without knowing their exact class** in advance.

----------

## 2️⃣ Method Overriding

**Definition:**  
When a **child class** has a method with the **same name as a method in the parent class**, but gives it a **new implementation**.

### Example:

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"  # Overrides parent method

dog = Dog()
print(dog.speak())  # Woof!

```

💡 **Key Point:**  
If the child class **does not** override the method, it will **use the parent's version**.

----------

## 3️⃣ Magic Methods

Magic methods (a.k.a. **dunder methods**) are special methods in Python that **start and end with double underscores**.  
They let you **customize** how objects behave with built-in functions and operators.

### Common Magic Methods:

#### `__str__`

-   Controls what `print(object)` displays.
    
-   Should return a **user-friendly** string.
    

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"📖 '{self.title}' with {self.pages} pages"

book = Book("Python Basics", 200)
print(book)  # 📖 'Python Basics' with 200 pages

```

#### `__len__`

-   Called by `len(object)`.
    

```python
    def __len__(self):
        return self.pages

print(len(book))  # 200

```

#### `__repr__`

-   **Developer-focused** representation (often used for debugging).
    
-   Should return a string that **could recreate the object**.
    

```python
    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"

print(repr(book))  # Book('Python Basics', 200)

```

💡 **Rule of Thumb:**

-   `__str__` → Human-friendly output
    
-   `__repr__` → Developer/debugging output
    

----------

## 4️⃣ Class Methods vs Static Methods

### **Class Method** (`@classmethod`)

-   Receives the **class itself** (`cls`) as the first argument.
    
-   Often used for **factory methods** (creating objects in alternative ways).
    

```python
class Student:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_fullname(cls, fullname):
        first_name = fullname.split()[0]
        return cls(first_name)

student = Student.from_fullname("Alice Johnson")
print(student.name)  # Alice

```

----------

### **Static Method** (`@staticmethod`)

-   **No automatic `self` or `cls` passed**.
    
-   Just a function that **belongs to a class** for organizational purposes.
    

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 3))  # 8

```

💡 Use `@staticmethod` when:

-   The method **does not need** class or instance data.
    
-   You just want to **group related functions** inside a class.
    

----------

## 🛠️ Practice Projects

### 1. Shape Class → Area Method for Circle, Square, Triangle
### 2. Book Class with `__str__` and `__len__`
### 3. MathUtils Class with Static Methods
