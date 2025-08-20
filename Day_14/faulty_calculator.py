import pdb

def calculator(a, b, operation):
    pdb.set_trace()  # Debugger starts here
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b   # ⚠️ This will cause error if b = 0
    else:
        return "Invalid Operation"

# Example runs
print(calculator(10, 5, "add"))   # Correct
print(calculator(10, 0, "div"))   # Faulty case → debug with pdb
