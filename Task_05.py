contacts = {}

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    
    if name in contacts:
        print(f"A contact with the name '{name}' already exists.")
    else:
        contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Contact for {name} added successfully!")

def view_contacts():
    if contacts:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")
    else:
        print("No contacts found.")

def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    found = False
    
    for name, details in contacts.items():
        if search_term.lower() == name.lower() or search_term == details['phone']:
            print(f"\nContact found:\nName: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
            found = True
            break
    
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Current details for {name}:")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")
        
        new_phone = input("Enter new phone number (leave blank to keep current): ")
        new_email = input("Enter new email (leave blank to keep current): ")
        new_address = input("Enter new address (leave blank to keep current): ")
        
        if new_phone:
            contacts[name]['phone'] = new_phone
        if new_email:
            contacts[name]['email'] = new_email
        if new_address:
            contacts[name]['address'] = new_address
        
        print(f"Contact for {name} updated successfully!")
    else:
        print(f"Contact with name '{name}' not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} deleted successfully!")
    else:
        print(f"Contact with name '{name}' not found.")

def contact_book():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

contact_book()
