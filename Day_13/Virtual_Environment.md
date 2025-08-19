### 2️⃣ Virtual Environment + Install External Module

-   Steps:
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # (Linux/Mac)
    venv\Scripts\activate     # (Windows)
    
    pip install requests
    pip freeze > requirements.txt
    
    ```
    
-   Example usage:
    
    ```python
    import requests
    
    response = requests.get("https://api.github.com")
    print(response.status_code)   # 200
    print(response.json())        # JSON data
    
    ```
    
