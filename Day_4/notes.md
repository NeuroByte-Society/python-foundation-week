# ✅ Day 4: Strings in Python

## 📘 Topics Covered

### 1. String Indexing and Slicing

Strings in Python are **sequences** of characters.  
Each character in a string has an **index**.

```python
text = "Hello"

# Indexing
print(text[0])  # H
print(text[-1]) # o (negative indexing from the end)

# Slicing
print(text[1:4])  # ell (includes index 1, 2, 3)
print(text[:3])   # Hel
print(text[2:])   # llo
````

---

### 2. String Methods

#### 🔹 `.lower()` and `.upper()`

Convert string to lowercase or uppercase.

```python
s = "Python"
print(s.lower())  # python
print(s.upper())  # PYTHON
```

#### 🔹 `.strip()`

Removes whitespace (or other characters) from both ends.

```python
msg = "  Hello World  "
print(msg.strip())  # "Hello World"
```

#### 🔹 `.replace()`

Replace part of a string with another.

```python
text = "I love Java"
print(text.replace("Java", "Python"))  # I love Python
```

#### 🔹 `.split()`

Split string into a list by a delimiter.

```python
data = "apple,banana,cherry"
print(data.split(","))  # ['apple', 'banana', 'cherry']
```

#### 🔹 `.find()`

Find index of the first occurrence of a substring.

```python
s = "welcome"
print(s.find("c"))  # 3
```

#### 🔹 `.count()`

Count number of times a substring appears.

```python
text = "banana"
print(text.count("a"))  # 3
```

---

### 3. f-Strings (String Formatting)

Used to embed variables inside strings easily.

```python
name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

You can also do expressions inside f-strings:

```python
price = 49.99
print(f"The price with tax is {price * 1.18:.2f}")  # 58.99
```

---

## 🧠 Mini Tasks

---

### 1. Count Vowels in a Sentence

```python
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in sentence if char in vowels)
print(f"Number of vowels: {count}")
```

### 2. Palindrome Checker

A palindrome reads the same forwards and backwards.

```python
text = input("Enter text: ")
cleaned = text.lower().replace(" ", "")
if cleaned == cleaned[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
```

---

## 🛠️ Mini Project: Word Counter

### 🎯 Objective:

Write a program that takes multi-line input from the user and reports:

* Total number of words
* Total number of lines
* Total number of characters (including spaces)

### ✅ Features:

* Takes input until user enters a special keyword like `"END"`
* Uses `.split()` for word counting
* Uses `len()` for character and line counting

### 💻 Code:

```python
print("Enter your text (type 'END' to stop):")

lines = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

full_text = "\n".join(lines)

# Word count
words = full_text.split()
word_count = len(words)

# Line count
line_count = len(lines)

# Character count
char_count = len(full_text)

print("\n📊 Word Count Results:")
print(f"Total Lines     : {line_count}")
print(f"Total Words     : {word_count}")
print(f"Total Characters: {char_count}")
```

### 📘 Explanation:

* `input()` reads each line.
* `"END"` is used to signal the end of input.
* `split()` splits on whitespace by default.
* `len()` gives counts of lists, strings, etc.
* `\n` is used to join lines into a single string for consistent counting.

---

### ✅ Summary

* Strings are **immutable sequences** in Python.
* You learned indexing, slicing, and **common string methods**.
* You practiced **string formatting** with `f-strings`.
* You built logic to **analyze and manipulate text**, including:

  * Checking for palindromes
  * Counting vowels
  * Building a full word/line/character counter

