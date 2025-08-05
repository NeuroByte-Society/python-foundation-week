## 🛠️ Mini Project: Contact Book (Add, Search, Delete)

### Code:

```python
contact_book = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contact_book[name] = phone
    print(f"✅ Contact {name} added.")

def search_contact():
    name = input("Enter name to search: ")
    if name in contact_book:
        print(f"{name}'s number is {contact_book[name]}")
    else:
        print("❌ Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"🗑️ Contact {name} deleted.")
    else:
        print("❌ Contact not found.")

def show_contacts():
    if not contact_book:
        print("📭 No contacts found.")
    else:
        print("📒 Contact List:")
        for name, phone in contact_book.items():
            print(f"{name}: {phone}")

# Menu
while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        show_contacts()
    elif choice == '5':
        print("👋 Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Try again.")

```

### Explanation:

-   A simple CLI-based contact book using dictionary.
    
-   Functions improve code organization: `add_contact()`, `search_contact()`, `delete_contact()`, `show_contacts()`.
    
-   The loop gives a continuous menu to operate the book.
    
