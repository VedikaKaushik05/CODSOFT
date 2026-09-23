contacts = []

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    if not all([name, phone, email, address]):
        print("All contact details are required.")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully.")


def view_contacts():
    if not contacts:
        print("No contacts saved.")
        return

    print("\n===== CONTACT LIST =====")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")


def search_contact():
    query = input("Enter name or phone number to search: ").strip().lower()

    results = [
        c for c in contacts
        if query in c["name"].lower() or query in c["phone"].lower()
    ]

    if not results:
        print("No matching contact found.")
        return

    for contact in results:
        print("\nName:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("Address:", contact["address"])


def update_contact():
    view_contacts()

    if not contacts:
        return

    try:
        number = int(input("Enter contact number to update: "))
        contact = contacts[number - 1]

    except (ValueError, IndexError):
        print("Invalid contact number.")
        return

    print("Press Enter to keep the existing value.")

    name = input(f"Name [{contact['name']}]: ").strip()
    phone = input(f"Phone [{contact['phone']}]: ").strip()
    email = input(f"Email [{contact['email']}]: ").strip()
    address = input(f"Address [{contact['address']}]: ").strip()

    if name:
        contact["name"] = name

    if phone:
        contact["phone"] = phone

    if email:
        contact["email"] = email

    if address:
        contact["address"] = address

    print("Contact updated successfully.")


def delete_contact():
    view_contacts()

    if not contacts:
        return

    try:
        number = int(input("Enter contact number to delete: "))
        removed = contacts.pop(number - 1)

    except (ValueError, IndexError):
        print("Invalid contact number.")
        return

    print(f"Contact '{removed['name']}' deleted successfully.")


while True:
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank you for using the Contact Management System.")
        break

    else:
        print("Invalid choice. Please select 1-6.")
