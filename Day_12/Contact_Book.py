import json

# Load existing contacts
try:
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = {}

# Add new contact
contacts["Alice"] = {"phone": "123-456-7890", "email": "alice@example.com"}

# Save back
with open("contacts.json", "w") as f:
    json.dump(contacts, f, indent=4)
