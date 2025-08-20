# 📍 NeuroByte Society – Python Bootcamp

## ✅ Day 14: Debugging & Testing  



## 📘 Topics Covered  

### 🔎 Debugging with `pdb`  
`pdb` stands for **Python Debugger**. It allows us to stop code execution and inspect what is happening step by step.  

**Why use pdb?**  
- Helps you find logical errors in your code.  
- Lets you pause the program and check variable values.  
- Allows you to run your code line by line.  

**Common Commands in pdb:**  
- `n` → Next line  
- `s` → Step into function  
- `c` → Continue execution until next breakpoint  
- `p variable` → Print value of a variable  
- `q` → Quit debugger  

**Example:**  
```python
import pdb

def divide(a, b):
    pdb.set_trace()  # set a breakpoint
    return a / b

print(divide(10, 2))
print(divide(10, 0))  # this will cause ZeroDivisionError
```

---

### 🧪 Unit Testing with `unittest`  
Unit testing is a way to automatically test small parts (units) of your program to make sure they work correctly.  

**Why use tests?**  
- Saves time by catching bugs early.  
- Ensures your code works as expected when you make changes.  
- Makes collaboration easier in real projects.  

**How to write a test:**  
```python
import unittest  
# 'import' → brings in external Python modules (pre-written code we can use)  
# 'unittest' → Python’s built-in module for testing code automatically


def is_prime(n):  
# 'def' → defines a new function  
# 'is_prime' → the function’s name (checks if a number is prime)  
# '(n)' → input parameter, the number we want to test

    if n < 2:  
        return False  
# 'if' → conditional check  
# 'n < 2' → prime numbers are 2 or greater, so if n is 0 or 1 (or negative), it’s not prime  
# 'return False' → immediately gives back False (not prime)

   for i in range(2, int(n**0.5) + 1):  
# 'for' → loop to check each possible divisor  
# 'i' → loop variable (possible divisor)  
# 'range(2, ...)' → starts checking from 2, since 1 divides everything  
# 'n**0.5' → square root of n (we only need to check up to sqrt(n))  
# 'int(...)' → converts the square root to an integer (since range only takes integers)  
# '+1' → include the upper bound in the check

         if n % i == 0:  
            return False  
# 'if' → check if n is divisible by i  
# 'n % i' → modulus operator, gives the remainder of n ÷ i  
# '== 0' → means no remainder, so i divides n evenly  
# 'return False' → n is not prime, exit immediately

    return True  
# If no divisors were found, the number is prime  
# Function ends by returning True

class TestPrime(unittest.TestCase):  
# 'class' → defines a group of related functions (methods)  
# 'TestPrime' → class name (we test prime number function here)  
# '(unittest.TestCase)' → inherits features from unittest so we can write tests easily

    def test_small_numbers(self):  
# Defines a test method (all test methods must start with 'test_')  
# 'self' → reference to the current object (needed in class methods)

        self.assertFalse(is_prime(1))  
# 'self.assertFalse(...)' → test that the inside expression is False  
# 'is_prime(1)' → checks if 1 is prime (should be False)

        self.assertTrue(is_prime(2))  
        self.assertTrue(is_prime(3))  
# 'self.assertTrue(...)' → test that the inside expression is True  
# Checks that 2 and 3 are correctly identified as primes


    def test_composites(self):  
# Another test method for composite (non-prime) numbers

        self.assertFalse(is_prime(4))  
        self.assertFalse(is_prime(9))  
# These should return False, since 4 and 9 are not prime


if __name__ == "__main__":  
# Special Python condition:  
# '__name__' → built-in variable that stores the module’s name  
# If we run this file directly, '__name__' becomes "__main__"  
# This ensures our tests only run when we execute this file directly

    unittest.main()  
# Runs all test methods inside the class TestPrime  
# It automatically reports which tests passed and which failed

```

**Running the test:**  
```bash
python -m unittest notes.py
```

---

## 🛠️ Practice Projects  
1️⃣ Debug a faulty calculator program using `pdb`.  
2️⃣ Write unit tests for a function that checks if a number is prime.  
3️⃣ Test and debug a small "student grading system" program to ensure it calculates averages and grades correctly.  
