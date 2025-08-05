
# ✅ Day 7: Functions + File Handling + Error Handling

## 📘 Topics



### 🔹 `def` Keyword & Return Values

```python
def greet(name):
    return f"Hello, {name}!"

```

#### ✅ Explanation:

-   `def` defines a function.
    
-   `return` sends back the result.
    
-   If no `return`, function returns `None`.
    

----------

### 🔹 Default Parameters

```python
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25 (5^2)
print(power(5, 3))   # 125 (5^3)

```

#### ✅ Explanation:

-   Default values avoid errors when arguments are missing.
    
-   Useful for optional parameters.
    

----------

### 🔹 Exception Handling (`try-except`)

```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)
except ZeroDivisionError:
    print("❌ Cannot divide by zero.")
except ValueError:
    print("❌ Please enter a valid number.")

```

#### ✅ Explanation:

-   `try`: Code to attempt.
    
-   `except`: Handles specific errors.
    
-   Prevents program crash during runtime issues.
    

----------

### 🔹 File Handling (.txt, .csv, .json)

----------

#### 📄 Read/Write Text File

```python
# Writing to a file
with open("notes.txt", "w") as file:
    file.write("Today I learned about file handling in Python.")

# Reading the file
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

```

✅ `with open()` auto-closes the file.  
`"w"`: write mode, `"r"`: read mode

----------

#### 📑 Working with CSV

```python
import csv

# Writing to CSV
with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])

# Reading from CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

```

✅ Use `csv` module for structured tabular data.

----------

#### 📁 Working with JSON

```python
import json

data = {"name": "Alice", "age": 25}

# Writing JSON
with open("data.json", "w") as file:
    json.dump(data, file)

# Reading JSON
with open("data.json", "r") as file:
    loaded = json.load(file)
    print(loaded)

```

✅ JSON is used for structured storage (like APIs, configs).

----------

## 🧠 Mini Tasks

#### 1️⃣ Prime Checker Function
#### 2️⃣ Safe Division using try-except


## 🛠️ Final Projects

#### 🔹 1. ATM Simulator
#### 🔹 2. To-Do List (w/ File Handling)
#### 🔹 3. File Reader + Word Counter
#### 🔹 4. JSON Contact Saver
