# contact_book.py

# Store contacts in a list of dictionaries
contacts = []


# Add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully!")


# Search for a contact by name
def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact

    return None


# Delete a contact by name
def delete_contact(name):
    contact = search_contact(name)

    if contact is not None:
        contacts.remove(contact)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


# View all contacts
def view_all():
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        print("\n========== ALL CONTACTS ==========")

        for contact in contacts:
            print(f"Name:  {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print("-" * 35)


# Main menu
while True:
    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        name = input("Enter name to search: ")
        contact = search_contact(name)

        if contact is not None:
            print("\nContact Found:")
            print(f"Name:  {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to delete: ")
        delete_contact(name)

    elif choice == "4":
        view_all()

    elif choice == "5":
        print("Thank you for using the Contact Book!")
        break

    else:
        print("Invalid choice. Please try again.")