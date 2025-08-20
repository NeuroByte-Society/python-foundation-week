
# **3️⃣ Student Grading System (with debugging)**

```python
import pdb

def calculate_average(marks):
    return sum(marks) / len(marks)   # ⚠️ Bug if marks list is empty

def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"

def grading_system(student_name, marks):
    pdb.set_trace()  # Debugging checkpoint
    avg = calculate_average(marks)
    grade = assign_grade(avg)
    return f"Student: {student_name}, Average: {avg:.2f}, Grade: {grade}"

# Example usage
print(grading_system("Alice", [90, 85, 92]))   # Expected: A
print(grading_system("Bob", [40, 50, 35]))     # Expected: F
print(grading_system("Charlie", []))           # ⚠️ Error → debug with pdb
```

👉 Learners can **debug when marks list is empty** (ZeroDivisionError).
They’ll realize they need to handle this case, e.g.:

```python
def calculate_average(marks):
    if len(marks) == 0:
        return 0   # or raise ValueError("No marks provided")
    return sum(marks) / len(marks)
```
