
# 🔢 Custom Mini Calculator with `lambda`, `map()`, and `filter()`

This note explores how to use **lambda functions**, along with **map()** and **filter()**, to build simple yet powerful operations like a mini calculator.

---

## 🔹 1. Lambda Functions Recap

Lambda functions are anonymous, one-liner functions.

```python
# Syntax
lambda arguments: expression
```

Example:

```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

---

## 🔹 2. Mini Calculator with `lambda`

Let’s define a basic calculator using lambda expressions for arithmetic operations.

### ✅ Code Example

```python
# Define operations using lambda
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Division by zero!"

# Example usage
print(add(10, 5))       # Output: 15
print(subtract(10, 5))  # Output: 5
print(multiply(10, 5))  # Output: 50
print(divide(10, 5))    # Output: 2.0
```

---

## 🔹 3. Use of `map()` in Calculator

`map()` can apply a lambda to a list of values.

### ✅ Example: Squaring a List

```python
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  # Output: [1, 4, 9, 16]
```

### ✅ Example: Adding 10 to All Elements

```python
nums = [5, 10, 15]
add_10 = list(map(lambda x: x + 10, nums))
print(add_10)  # Output: [15, 20, 25]
```

---

## 🔹 4. Use of `filter()` in Calculator

`filter()` filters elements from a list using a condition.

### ✅ Example: Filter Even Numbers

```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]
```

### ✅ Example: Filter Positive Numbers

```python
nums = [-5, -2, 0, 1, 4, -3]
positives = list(filter(lambda x: x > 0, nums))
print(positives)  # Output: [1, 4]
```

---

## 🔹 5. Combine All: Custom Operation on User Input

```python
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# Square all even numbers
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print("Squared Evens:", result)
```

🧠 **What this does**:
- Takes space-separated input numbers
- Filters even numbers
- Squares them using `map()`

---

## ✅ Practice Ideas

1. Build a lambda-based calculator that accepts operation type as input (`+`, `-`, `*`, `/`).
2. Use `filter()` to extract numbers divisible by 3 from a list.
3. Use `map()` to convert a list of strings to uppercase.

---

🚀 Practice combining `lambda`, `map()`, `filter()` with custom logic to build more powerful operations!
