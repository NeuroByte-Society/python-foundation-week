# ✅ Day 12: File Handling - CSV & JSON

## 📘 Topics

### 1. Reading/Writing `.txt` Files

-   Use `open()` with modes:
    -   `'r'` → read
    -   `'w'` → write (overwrites existing content)
    -   `'a'` → append (adds to existing content)
-   Example:

``` python
with open("notes.txt", "w") as f:
    f.write("Hello, this is a text file!")
```

### 2. Reading/Writing `.csv` Files

-   Use the built-in **csv module**.
-   CSV stands for *Comma Separated Values*.
-   Example:

``` python
import csv

# Writing
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 21])
    writer.writerow(["Bob", 22])

# Reading
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### 3. Reading/Writing `.json` Files

-   Use the built-in **json module**.
-   JSON stands for *JavaScript Object Notation*.
-   Example:

``` python
import json

# Writing
data = {"name": "Alice", "age": 21}
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Reading
with open("data.json", "r") as f:
    loaded_data = json.load(f)
    print(loaded_data)
```

------------------------------------------------------------------------

Here’s a **summary of today’s topics (Day 12: File Handling - CSV & JSON):**

---

### 📘 Summary

1. **Text Files (`.txt`)**

   * Open files using `open()` with modes:

     * `'r'` → read
     * `'w'` → write (overwrites file)
     * `'a'` → append (adds at end)
   * Use `with open(...) as f:` for safe handling.

2. **CSV Files (`.csv`)**

   * Use **`csv` module** for structured data storage.
   * Data is stored as rows and columns separated by commas.
   * Functions:

     * `csv.writer()` → write rows
     * `csv.reader()` → read rows

3. **JSON Files (`.json`)**

   * Use **`json` module** to store structured data (dictionary-like).
   * Functions:

     * `json.dump(data, file)` → write to file
     * `json.load(file)` → read from file
   * Useful for storing data in key-value format.

---

### 🛠️ Mini Projects

* **Student Data to CSV** → Store multiple student records in `.csv`.
* **Contact Book in JSON** → Read & update contacts with phone/email.
* **Diary App with `.txt`** → Log daily entries as plain text.


