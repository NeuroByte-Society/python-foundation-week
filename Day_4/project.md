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

