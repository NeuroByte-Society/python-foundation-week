import csv

students = [
    ["Name", "Age", "Grade"],
    ["Alice", 21, "A"],
    ["Bob", 22, "B"],
    ["Charlie", 20, "A"]
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)
