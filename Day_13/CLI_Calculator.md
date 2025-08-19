### 3️⃣ Simple Command-line Calculator Using Custom Modules

-   **Folder structure**:
    
    ```
    calculator_app/
        __init__.py
        math_utils.py
        main.py
    
    ```
    
-   `math_utils.py`
    
    ```python
    def add(a, b): return a + b
    def subtract(a, b): return a - b
    def multiply(a, b): return a * b
    def divide(a, b): return a / b if b != 0 else "Error: Division by zero"
    
    ```
    
-   `main.py`
    
    ```python
    import math_utils
    
    def main():
        print("🔢 Simple Calculator")
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Choose operation (+, -, *, /): ")
    
        if op == "+":
            print("Result:", math_utils.add(a, b))
        elif op == "-":
            print("Result:", math_utils.subtract(a, b))
        elif op == "*":
            print("Result:", math_utils.multiply(a, b))
        elif op == "/":
            print("Result:", math_utils.divide(a, b))
        else:
            print("Invalid operation")
    
    if __name__ == "__main__":
        main()
    
    ```
    
    ✅ Run it:
    
    ```bash
    python main.py
    
    ```
    
