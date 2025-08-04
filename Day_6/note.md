# ✅ Day 6: Dictionaries + Nested Data Structures

## 📘 Topics

### 1. Dictionaries: `{key: value}` Basic Operations

Dictionaries in Python are unordered collections of key-value pairs. Keys must be unique and immutable, while values can be of any data type.

```python
person = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
}
````

#### Accessing Values

```python
print(person["name"])  # Output: Alice
```

#### Adding or Updating Values

```python
person["city"] = "Delhi"         # Add new key-value
person["age"] = 26               # Update value
```

#### Removing Key-Value Pairs

```python
del person["email"]
```

---

### 2. Dictionary Methods

#### `.get(key, default)`

Safe way to get a value. Returns `None` or default if key doesn't exist.

```python
print(person.get("email", "Not available"))
```

#### `.keys()`, `.values()`, `.items()`

```python
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 26, 'Delhi'])
print(person.items())   # dict_items([('name', 'Alice'), ('age', 26), ('city', 'Delhi')])
```

---

### 3. Looping Through Dictionaries

```python
for key in person:
    print(key, "->", person[key])

# OR

for key, value in person.items():
    print(f"{key}: {value}")
```

---

### 4. Nested Dictionaries and Lists

#### Example 1: Dictionary with List

```python
student = {
    "name": "Bob",
    "subjects": ["Math", "Science", "English"]
}
```

#### Example 2: Dictionary of Dictionaries

```python
students = {
    "101": {"name": "Alice", "grade": "A"},
    "102": {"name": "Bob", "grade": "B"}
}
```

#### Access Nested Values

```python
print(students["101"]["name"])  # Output: Alice
```

---

## 🧠 Mini Tasks

### ✅ Task 1: Phone Directory

Create a dictionary to store names and phone numbers. Allow retrieval of a number by name

### ✅ Task 2: Quiz Dictionary

Create a dictionary where keys are questions and values are answers.


## 🛠️ Mini Project: Contact Book

A command-line app where user can:

* Add new contact
* Search by name
* Delete contact


## 📝 Practice Problems

1. **Create a dictionary of 5 countries and their capitals. Allow user to input a country and get its capital.**
2. **Write a function to count the frequency of characters in a string using a dictionary.**
3. **Create a nested dictionary to store student marks in 3 subjects. Calculate average marks for each student.**
4. **Create a dictionary from two lists: one of keys and one of values.**
5. **Create a dictionary of employees with salary. Display names of employees earning more than ₹50,000.**

---

## 💡 Summary

* Dictionaries store key-value pairs.
* You can nest dictionaries and lists to represent complex data.
* Common methods: `.get()`, `.items()`, `.keys()`, `.values()`
* Looping and modifying data is flexible and readable.
* Great for contact books, quiz games, configuration data, etc.

---
