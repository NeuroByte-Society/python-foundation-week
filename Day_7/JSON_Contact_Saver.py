### 🔹 4. JSON Contact Saver


import json

def save_contact(name, number):
    contact = {"name": name, "number": number}

    try:
        with open("contacts.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(contact)

    with open("contacts.json", "w") as file:
        json.dump(data, file, indent=2)

    print("✅ Contact saved.")

def show_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
            for c in contacts:
                print(f"{c['name']}: {c['number']}")
    except FileNotFoundError:
        print("📭 No contacts saved.")

# CLI
while True:
    print("\n--- JSON Contact Saver ---")
    print("1. Add Contact\n2. View Contacts\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        number = input("Number: ")
        save_contact(name, number)
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        break
    else:
        print("⚠️ Invalid option")
