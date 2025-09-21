def adding_contact(contacts_list, contact_name, contact_email, contact_phone):
    contact = {"name": contact_name, "email": contact_email, "phone": contact_phone, "favourite": False}
    contacts_list.append(contact)
    return(f"Contact '{contact_name}' has been added")



contacts_list = []

while True:
    print("\n Menu to for managing your contact list")
    print("1. Add a new contact")
    print("2. Update a contact")
    print("3. See contacts list")
    print("4. Tag/Untage contact as favourite")
    print("5. Check favourite contacts list")
    print("6. Delete completed task(s)")
    print("7. Exit")

    user_input = input("Please choose an option: ")

    if user_input == "1":
        contact_name = input("Please add name: ")
        contact_email = input("Please add email: ")
        contact_phone = input("Please add phone number: ")
        adding_contact(contacts_list, contact_name, contact_email, contact_phone)
    elif user_input == "7":
        break