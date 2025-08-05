# 2️⃣ Safe Division using try-except

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "❌ Cannot divide by zero"
    except TypeError:
        return "❌ Invalid input type"

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # Error message

```

✅ Protects division from crashing due to zero or invalid types.
