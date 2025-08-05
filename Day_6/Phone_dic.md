## 🧠 Mini Task 1: Phone Directory

### Code:
```python
phone_directory = {
    "Alice": "9876543210",
    "Bob": "8765432109",
    "Charlie": "7654321098"
}

# Accessing a number
print("Alice's number:", phone_directory["Alice"])

# Adding a new contact
phone_directory["David"] = "6543210987"

# Updating a contact
phone_directory["Alice"] = "9999999999"

# Deleting a contact
del phone_directory["Charlie"]

# Display all contacts
print("\nUpdated Phone Directory:")
for name, number in phone_directory.items():
    print(f"{name}: {number}")

```

### Explanation:

-   A `dictionary` is used to map names to phone numbers.
    
-   `.items()` helps loop through both key and value.
    
-   Adding, updating, and deleting keys is easy and intuitive with the dictionary.
