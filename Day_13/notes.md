# ✅ Day 13: Modules + Packages + Virtual Environments

📍 **NeuroByte Society – Python Bootcamp**

Today we explored how to organize Python code into **modules** and **packages**, and how to use **virtual environments** for project isolation. These are essential skills for writing reusable, maintainable, and professional Python applications.

---

## 📘 Topics

### 1. Custom Modules & Imports

* **What is a module?**
  A **module** is just a Python file (`.py`) that contains functions, classes, or variables you can reuse.
  Example:

  ```python
  # file: math_utils.py
  def add(a, b):
      return a + b

  def multiply(a, b):
      return a * b
  ```

  Using this module:

  ```python
  import math_utils

  print(math_utils.add(5, 3))       # 8
  print(math_utils.multiply(4, 2))  # 8
  ```

  ✅ This helps avoid repeating the same code across multiple files.

---

### 2. Create Package with `__init__.py`

* **What is a package?**
  A **package** is a folder containing multiple Python modules, with a special file `__init__.py`.

* Example:
  Folder structure:

  ```
  my_package/
      __init__.py
      math_utils.py
      string_utils.py
  ```

  ```python
  # file: my_package/math_utils.py
  def square(x):
      return x * x
  ```

  ```python
  # file: my_package/string_utils.py
  def capitalize_words(s):
      return s.title()
  ```

  Usage:

  ```python
  from my_package import math_utils, string_utils

  print(math_utils.square(5))             # 25
  print(string_utils.capitalize_words("hello world"))  # "Hello World"
  ```

  ✅ Packages allow **organization** like folders for your code.

---

### 3. Use of `pip`, `venv`, `requirements.txt`

* **pip** → Python’s package installer.
  Example:

  ```bash
  pip install requests
  ```

* **Virtual Environment (venv)** → Isolates dependencies for each project.

  ```bash
  # Create venv
  python -m venv venv

  # Activate venv (Windows)
  venv\Scripts\activate

  # Activate venv (Mac/Linux)
  source venv/bin/activate
  ```

* **requirements.txt** → Saves project dependencies.

  ```bash
  pip freeze > requirements.txt
  pip install -r requirements.txt
  ```

  ✅ This makes your project **portable and reproducible**.

---

## 🛠️ Projects

### 1️⃣ Create a Utility Package (`math_utils`, `string_utils`)

* **Folder structure**:

  ```
  utilities/
      __init__.py
      math_utils.py
      string_utils.py
  ```
  
### 2️⃣ Build a Virtual Environment + Install External Module

* Steps:

  ```bash
  python -m venv venv
  source venv/bin/activate  # (Linux/Mac)
  venv\Scripts\activate     # (Windows)

  pip install requests
  pip freeze > requirements.txt
  ```

### 3️⃣ Simple Command-line Calculator Using Custom Modules

* **Folder structure**:

  ```
  calculator_app/
      __init__.py
      math_utils.py
      main.py
  ```

## 🎯 Key Takeaways

* **Modules** = single Python files for reuse.
* **Packages** = organized folders with multiple modules.
* **Virtual environments** = isolate dependencies per project.
* **requirements.txt** = share project dependencies easily.
* ✅ These skills are **fundamental** for real-world Python projects.

---
