# ✅ Day 2: Operators + Conditions   

---

## 📘 Topics Covered

### 🔢 Arithmetic Operators
Used to perform mathematical operations:

- `+` : Addition  
- `-` : Subtraction  
- `*` : Multiplication  
- `/` : Division (float)  
- `//` : Floor Division  
- `%` : Modulus (Remainder)  
- `**` : Exponentiation (Power)

```python
a = 10
b = 3
print(a + b)   # 13
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
````

---

### ⚖️ Comparison Operators

Used to compare values (returns True/False):

* `==` : Equal to
* `!=` : Not equal to
* `<`  : Less than
* `>`  : Greater than
* `<=` : Less than or equal to
* `>=` : Greater than or equal to

```python
x = 5
y = 10
print(x == y)   # False
print(x < y)    # True
```

---

### 🔍 Logical Operators

Used to combine conditional statements:

* `and` : True if both conditions are True
* `or`  : True if at least one condition is True
* `not` : Inverts the result

```python
age = 20
print(age > 18 and age < 30)   # True
print(age < 18 or age > 65)    # False
print(not(age < 18))           # True
```

---

### 🧭 Conditional Statements

Control flow based on conditions:

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
```

#### 🔄 Nested Conditions

```python
num = 7
if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
```

---

## 🧠 Mini Task

##### 1. Odd/Even Checker
##### 2. Grade Calculator

## 🛠️ Mini Project:

##### Simple Login System


---
