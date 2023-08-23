# Define a class to store individual contact information
class Contacts:
    def __init__(self, name = None, phone_number = None, email_address = None, address = None):
        # Initialize contact attributes
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address
        self.address = address

# Define a class to manage contacts
class ContactManager:
    def __init__(self):
        # Initialize the list to store contacts
        self.contacts = []

    def add_contact(self, name, phone_number, email_address, address):
        # Check if the phone number already exists in the contacts
        if any(contact.phone_number == phone_number for contact in self.contacts):
            print("A contact with the same phone number already exists.")
        else:
            # Create a Contacts instance and add it to the list of contacts
            contact = Contacts(name, phone_number, email_address, address)
            self.contacts.append(contact)
            print("Contact Added Successfully")

    def view_all_contacts(self):
        if not self.contacts:
            # If there are no contacts, print a message indicating that no contacts were found
            print("No Contacts Found.")
        else:
            # If there are contacts, loop through the list and display each contact's details
            for idx, contact in enumerate(self.contacts):
                # Display contact details
                print("\nIndex:", idx + 1)
                print("Name:", contact.name)
                print("Phone Number:", contact.phone_number)
                print("Email Address:", contact.email_address)
                print("Address:", contact.address)

    def search_contact(self, data):
        # Use list comprehension to filter contacts matching the search criteria
        result = [contact for contact in self.contacts if str(data).lower() in contact.name.lower() or str(data) in str(contact.phone_number)]
 
        if not result:
            # If no contacts match the search criteria, print a message
            print("\nNo Contacts Found")
        else:
            # If matching contacts are found, display their details
            print("\nContacts with (name/phone_number):", data)
            for contact in result:
                print("\nName:", contact.name)
                print("Phone Number:", contact.phone_number)
                print("Email Address:", contact.email_address)
                print("Address:", contact.address)

    def delete_contact(self, name):
        # Initialize a count to keep track of how many contacts were deleted
        deleted_count = 0
        
        # Loop through each contact in the list of contacts
        for contact in self.contacts:
            # Check if the name of the contact matches the input name
            if contact.name.lower() == name.lower():
                # Remove the matching contact from the list
                self.contacts.remove(contact)
                # Increment the count of deleted contacts
                deleted_count += 1
        
        # Check if any contacts were deleted
        if deleted_count > 0:
            # Print a success message with the deleted contact's name
            print("Contact '{}' deleted successfully!".format(name))
        else:
            # Print a message indicating that no matching contact was found to delete
            print("No contact found to delete.")

# Main function
if __name__ == "__main__":
    # Create an instance of ContactManager
    contact_manager = ContactManager()

    # Add sample contacts
    contact_manager.add_contact("Anjali", 9876543210, "anjalikumar@gmail.com", "1234 Gali No. 5, Nanded")
    contact_manager.add_contact("Faizen", 7890123456, "faizen@gmail.com", "5678 Street No. 8, Mumbai")
    contact_manager.add_contact("Komal", 9012345678, "komal@gmail.com", "9876 Lane No. 3, Nipani")
    contact_manager.add_contact("Nisarg mehata", 3456789012, "nisragmehata@gmail.com", "4567 Road No. 12, Pune")

    # Display all contacts
    print("\n===== All Contacts =====")
    contact_manager.view_all_contacts()

    # Search for contacts with a given name
    print("\n===== Search Results for 'komal' =====")
    contact_manager.search_contact("komal")

    # Search for contacts with a given phone number
    print("\n===== Search Results for 9012345678 =====")
    contact_manager.search_contact(9012345678)

    # Delete a contact by name
    print("\n===== Deleting 'Komal' =====")
    contact_manager.delete_contact("Komal")

    # Display all contacts after deletion
    print("\n===== All Contacts after Deletion =====")
    contact_manager.view_all_contacts()

    # Search for contacts with a given phone number
    print("\n===== Search Results for 3456789012 =====")
    contact_manager.search_contact(3456789012)
