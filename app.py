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
def wait_for_enter():
    input()

def update_contact(contacts_list, contact_index, contact_new_name, contact_new_email, contact_new_phone):
    contacts_index_adjust = int(contact_index) -1
    if contacts_index_adjust >= 0 and contacts_index_adjust < len(contacts_list):
        contacts_list[contacts_index_adjust]["name"] = contact_new_name
        contacts_list[contacts_index_adjust]["email"] = contact_new_email
        contacts_list[contacts_index_adjust]["phone"] = contact_new_phone
        if contact_new_name != contact_name:
            print(f"Contact {contact_index} renamed to {contact_new_name}")
            if contact_new_email != contact_email:
                print(f"Contact {contact_index} new email set to {contact_new_email}")
                if contact_new_phone != contact_phone:
                    print(f"Contact {contact_index} new phone set to {contact_new_phone}")
    else:
        print("\nContact chosen does not exist")
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
    elif user_input == "3":
        check_contacts(contacts_list)
        contact_index = input("Select the number of the contact you'd like to update: ")
        print("\n Hit enter if you wish the attribute remains the same")
        contact_new_name = input("\nPlease rename your contact: ")
        contact_new_phone = input("\nPlease provide new phone number: ")
        contact_new_email = input("\nPlease provide new email: ")
        update_contact(contacts_list, contact_index, contact_new_name, contact_new_email, contact_new_phone)
    elif user_input == "7":
        break