
# ✅ Day 3: Loops + range()

## 📘 Topics Covered

### 🔁 1. Loops in Python

Loops are used to execute a block of code repeatedly.

#### ➤ `while` loop

The `while` loop runs **as long as a condition is True**.

```python
i = 1
while i <= 5:
    print(i)
    i += 1
````

* Starts from `i = 1`.
* Runs the loop body while `i <= 5`.
* `i += 1` updates `i` each time to avoid infinite loops.

#### ➤ `for` loop

Used to **iterate over sequences** like lists, strings, or ranges.

```python
for i in range(1, 6):
    print(i)
```

* `range(1, 6)` generates numbers 1 to 5.
* Each number is assigned to `i` one at a time.

---

### 📏 2. `range(start, stop, step)`

Generates a sequence of numbers.

* `start`: where the sequence starts (default is 0)
* `stop`: **up to but not including** this number
* `step`: increment between numbers (default is 1)

```python
range(0, 10, 2)  # 0, 2, 4, 6, 8
```

---

### 🚦 3. Loop Control Statements

#### ➤ `break`

Exits the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

#### ➤ `continue`

Skips the current iteration and moves to the next one.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

#### ➤ `pass`

A placeholder when code is syntactically required but you don’t want any action.

```python
for i in range(5):
    if i == 3:
        pass  # No action
    print(i)
```

---

## 🧠 Mini Task

#### 🔢 1. Multiplication Table of a Number
#### ➕ 2. Sum of Numbers from 1 to `n`

## 🛠️ Mini Project:
#### Number Guessing Game


---

### ✅ Summary

| Concept      | Description                       |
| ------------ | --------------------------------- |
| `while` loop | Repeats while a condition is true |
| `for` loop   | Iterates over a sequence          |
| `range()`    | Generates number sequences        |
| `break`      | Exits loop early                  |
| `continue`   | Skips current iteration           |
| `pass`       | Does nothing (placeholder)        |

---

🔁 Mastering loops is critical in any programming journey — they help in automation, iteration, and control of logic flow.

