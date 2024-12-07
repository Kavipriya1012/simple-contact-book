contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {'Phone': phone, 'Email': email}
    print(f"Contact for {name} added.")

def view_contacts():
    if contacts:
        print("\nContacts:")
        for name, info in contacts.items():
            print(f"{name}: Phone - {info['Phone']}, Email - {info['Email']}")
    else:
        print("No contacts found.")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}: Phone - {contacts[name]['Phone']}, Email - {contacts[name]['Email']}")
    else:
        print("Contact not found.")

def remove_contact():
    name = input("Enter name to remove: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} removed.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            remove_contact()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

