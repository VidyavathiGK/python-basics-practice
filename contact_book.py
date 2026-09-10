def contact_book():
    contacts = {}
    
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. View All Contacts")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            contacts[name] = phone
            print(f"Contact '{name}' added successfully!")
            
        elif choice == '2':
            name = input("Enter name to search: ").strip()
            if name in contacts:
                print(f"Phone number for {name}: {contacts[name]}")
            else:
                print(f"Contact '{name}' not found.")
                
        elif choice == '3':
            if not contacts:
                print("Contact book is empty.")
            else:
                print("\nSaved Contacts:")
                for name, phone in contacts.items():
                    print(f"- {name}: {phone}")
                    
        elif choice == '4':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice!!. Please choose between 1 and 4.")

if __name__ == "__main__":
    contact_book()















