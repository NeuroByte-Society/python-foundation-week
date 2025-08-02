# 🛠️ Mini Project: Student Database using List of Tuples
## Goal: Create a student database that stores each student as a tuple: (name, mark)

```python

# Student Database
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]

# Print all students
for name, mark in students:
    print(f"{name} scored {mark}")

# Find top scorer
topper = max(students, key=lambda student: student[1])
print(f"Top Scorer: {topper[0]} with {topper[1]} marks")
```

## Extension Ideas:

* Add input for new students.
* Remove students by name.
* Search student by name.

