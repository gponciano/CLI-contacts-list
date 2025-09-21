def adding_contact(contacts_list, contact_name, contact_email, contact_phone):
    contact = {"name": contact_name, "email": contact_email, "phone": contact_phone, "favourite": False}
    contacts_list.append(contact)
    return(f"Contact '{contact_name}' has been added")

def check_contacts(contacts_list):
    print("\n Check your current contact list:")
    for index, contact in enumerate(contacts_list, start=1):
        favourite = "✔" if contact["favourite"] else "Regular contact"
        contact_name = contact["name"]
        contact_email = contact["email"]
        contact_phone = contact["phone"]
        print(f"{index}. Name: {contact_name},  Email: {contact_email},  Phone: {contact_phone},  Status: {favourite}")
    return

contacts_list = []

while True:
    print("\n Menu to for managing your contact list")
    print("1. Add a new contact")
    print("2. See contacts list")
    print("3. Update a contact")
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
    elif user_input == "2":
        check_contacts(contacts_list)
    
    elif user_input == "7":
        break