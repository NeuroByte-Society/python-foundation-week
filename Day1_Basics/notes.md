# 🐍 Day 1 - Python Basics

---

### 📌 print() and input()

- The `print()` function displays output:
```python
print("your variable")
````

* The `input()` function takes input from the user:

```python
input("What do you want from the user?")
```

---

### 🧠 Identifiers

> An **identifier** is the name given to any entity in Python to uniquely identify it — variables, functions, classes, etc.

---

### 💡 Variables & Naming Rules

> A **variable** is a name referring to a memory location.

Example:

```python
a = 2 
b = "larry"
```

**Note:**
Variables are specific types of identifiers.

**Naming Rules:**

1. Can contain alphabets, digits, and underscores.
2. Must start with an alphabet or underscore.
3. Cannot start with a digit.
4. Whitespace is not allowed in variable names.

---

### 📚 Data Types

Python has the following common data types:

* `int` – Integers
* `float` – Floating point numbers
* `str` – Strings
* `bool` – Booleans
* `NoneType` – None

Example:

```python
a = 6       # int
b = 8.7     # float 
c = "larry" # string
d = True    # boolean
e = None    # NoneType

print(type(a), type(b), type(c), type(d), type(e))
```

---

### 🔄 Type Conversion in Python

> Type conversion means changing the data type of a value from one type to another.

#### Types:

1. **Implicit Conversion** – done automatically by Python
2. **Explicit Conversion** – done manually using functions like `int()`, `str()`, etc.

---

#### 🔧 Explicit Type Conversion Functions

| Function   | Converts To           |
| ---------- | --------------------- |
| `int(x)`   | Integer               |
| `float(x)` | Floating Point Number |
| `str(x)`   | String                |
| `bool(x)`  | Boolean               |
| `list(x)`  | List                  |
| `tuple(x)` | Tuple                 |

---

#### ✨ Examples:

```python
x = "10"
y = int(x)         # "10" ➜ 10 (int)

a = 3.14
b = int(a)         # 3.14 ➜ 3

c = 100
d = str(c)         # 100 ➜ "100"

n = 123
m = bool(n)

print("before :-", type(x), type(a), type(c), type(n))
print("after  :-", type(y), type(b), type(d), type(m))
```

