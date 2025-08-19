### 1️⃣  Utility Package (`math_utils`, `string_utils`)

-   **Folder structure**:
    
    ```
    utilities/
        __init__.py
        math_utils.py
        string_utils.py
    
    ```
    
-   `math_utils.py`
    
    ```python
    def factorial(n):
        return 1 if n == 0 else n * factorial(n-1)
    
    ```
    
-   `string_utils.py`
    
    ```python
    def reverse_string(s):
        return s[::-1]
    
    ```
    
-   Usage:
    
    ```python
    from utilities import math_utils, string_utils
    
    print(math_utils.factorial(5))   # 120
    print(string_utils.reverse_string("hello"))  # "olleh"
    
    ```
    
