## 🧠 Mini Tasks


#### 1️⃣ Prime Checker Function

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Example
print(is_prime(7))  # True
print(is_prime(10)) # False

```

✅ Efficient using `sqrt(n)` range. Returns boolean result.
