# ✅ Day 5: Lists + Tuples + Sets

## 📘 Topics

### 🔹 Lists
A **list** is an ordered, mutable collection of items in Python.

**Creating a List**
```python
students = ["Alice", "Bob", "Charlie"]
marks = [85, 90, 78]
````

**Common Methods**

| Method       | Description                       | Example            |
| ------------ | --------------------------------- | ------------------ |
| `.append()`  | Adds an element at the end        | `marks.append(95)` |
| `.remove(x)` | Removes the first occurrence of x | `marks.remove(90)` |
| `.sort()`    | Sorts list in ascending order     | `marks.sort()`     |

**Slicing**

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # Output: [20, 30, 40]
```

---

### 🔸 Tuples

A **tuple** is an ordered, **immutable** collection.

**Creating a Tuple**

```python
student = ("Alice", 85)
```

**Accessing Tuple Values**

```python
name = student[0]
score = student[1]
print(name, score)  # Output: Alice 85
```

**Deep Explanation**:

* Tuples cannot be changed once created.
* Useful when you want **read-only** data structures.
* Can be used as keys in dictionaries if they only contain immutable types.

---

### 🔸 Sets

A **set** is an unordered collection of **unique** elements.

**Creating a Set**

```python
fruits = {"apple", "banana", "cherry"}
```

**Common Set Methods**

| Method       | Description                            | Example                   |
| ------------ | -------------------------------------- | ------------------------- |
| `.add(x)`    | Adds element x                         | `fruits.add("orange")`    |
| `.remove(x)` | Removes element x (error if not found) | `fruits.remove("banana")` |

**Set Uniqueness**

```python
nums = {1, 2, 2, 3}
print(nums)  # Output: {1, 2, 3}
```

---

## 🧠 Mini Task: Student Marks

**Task**:

1. Store student names and marks.
2. Find the top scorer.
---

## 🛠️ Mini Project: Student Database using List of Tuples

**Goal**: Create a student database that stores each student as a tuple: `(name, mark)`
