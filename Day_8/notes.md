
# 🐍 Python Foundation Week – Functions Deep Dive + Recursion

---

## 🔹 1. **Function Scope: Local vs Global Variables**

### ▶ Local Variables:

Variables defined **inside a function**. They **exist only within** that function.

```python
def greet():
    message = "Hello!"  # Local variable
    print(message)

greet()
# print(message)  # ❌ Error: message is not defined outside
```

### ▶ Global Variables:

Defined **outside all functions**. Can be accessed anywhere.

```python
name = "Alice"  # Global variable

def say_hello():
    print("Hello,", name)

say_hello()
```

### ⚠ Modifying Global Variable Inside a Function

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1
```

🧠 **Tip**: Use `global` cautiously; prefer returning values instead.

---

## 🔹 2. **`*args` and `**kwargs` Usage**

### ▶ `*args` → for **non-keyword variable-length arguments** (tuple)

```python
def add(*args):
    return sum(args)

print(add(1, 2, 3))  # 6
print(add(5, 10))    # 15
```

> Think of `*args` as a way to accept multiple unnamed values.

### ▶ `**kwargs` → for **keyword variable-length arguments** (dict)

```python
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=25)
# name: Alice
# age: 25
```

> Think of `**kwargs` as a way to accept key=value pairs.

---

## 🔹 3. **Recursion: base case + recursive step**

A function calling **itself** to solve smaller instances of a problem.

### ⚙ Example: Factorial

```python
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive step

print(factorial(5))  # 120
```

### 🧠 Key Points:

* Must have a **base case** to stop.
* Must **move toward** the base case.

### ⚠ Recursive vs Iterative

```python
# Iterative factorial
def factorial_iter(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
```

---

## 🔹 4. **Lambda (Anonymous Functions)**

Lambda creates **one-liner anonymous functions**.

```python
square = lambda x: x * x
print(square(5))  # 25
```

### 🔸 Syntax:

```python
lambda arguments: expression
```

> ⚠ Cannot contain statements or multiple expressions.

---

## 🔹 5. **map(), filter(), reduce()**

These are **functional programming tools**.

### ✅ `map(function, iterable)`

```python
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  # [1, 4, 9, 16]
```

### ✅ `filter(function, iterable)`

```python
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]
```

### ✅ `reduce(function, iterable)`

```python
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # 24
```

### 🔍 Summary Table:

| Function | Input                             | Output            |
| -------- | --------------------------------- | ----------------- |
| `map`    | function, iterable                | modified iterable |
| `filter` | function (returns bool), iterable | filtered iterable |
| `reduce` | function (2 args), iterable       | single result     |

---

## ✅ Mini Practice

1. Write a function that sums any number of arguments using `*args`.
2. Write a recursive function for the Fibonacci sequence.
3. Use `map()` and `lambda` to cube numbers in a list.
4. Use `filter()` to get strings with length > 3 from a list.
5. Use `reduce()` to find the maximum of a list.

---

Happy Coding! 🚀
