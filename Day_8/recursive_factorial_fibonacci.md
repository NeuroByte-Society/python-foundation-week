
# 🔁 Recursive Factorial & Fibonacci Generator

Understanding recursion is a key part of mastering functions in Python. Here we explore two classic recursive problems:

---

## 🔹 1. Recursive Factorial Function

### ❓ What is Factorial?
The **factorial** of a number `n` (written as `n!`) is the product of all positive integers less than or equal to `n`.

**Example**:  
`5! = 5 × 4 × 3 × 2 × 1 = 120`

### 🔄 Recursive Logic

- **Base Case**: If `n == 0`, return 1 (by definition `0! = 1`).
- **Recursive Step**: Multiply `n * factorial(n - 1)`

### ✅ Python Code

```python
def factorial(n):
    if n == 0:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive step

# Example usage
print(factorial(5))  # Output: 120
```

---

## 🔹 2. Recursive Fibonacci Generator

### ❓ What is Fibonacci?
The **Fibonacci sequence** is a series where each number is the sum of the two preceding ones.

**Sequence**: `0, 1, 1, 2, 3, 5, 8, 13, ...`

**Formula**:
- `fib(0) = 0`
- `fib(1) = 1`
- `fib(n) = fib(n-1) + fib(n-2)`

### 🔄 Recursive Logic

- **Base Case**: If `n == 0` → return 0, if `n == 1` → return 1
- **Recursive Step**: return `fibonacci(n-1) + fibonacci(n-2)`

### ✅ Python Code

```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Print first 10 Fibonacci numbers
for i in range(10):
    print(fibonacci(i), end=' ')
# Output: 0 1 1 2 3 5 8 13 21 34
```

---

## ⚠ Notes on Recursion Efficiency

- Recursive Fibonacci is **not efficient** for large `n` due to repeated calculations.
- Use **memoization** or **iteration** for large values.

### 🔧 Tip: Memoized Fibonacci (Optional Advanced)

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

---

Happy Learning! 🧠✨
