# phone_directory.py

# Dictionary of contacts
contacts = {
    "Amara": "0821112222",
    "Sipho": "0832223333",
    "Lerato": "0843334444"
}

# Ask the user for a friend's name
name = input("Enter the name of the friend you want to look up: ")

# Search for the contact
if name in contacts:
    print(f"Found! {name}'s number is {contacts[name]}")
else:
    print("Contact not found.")