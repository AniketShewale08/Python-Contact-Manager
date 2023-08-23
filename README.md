# Python-Contact-Manager

#Contact Management System Implementation

1. Introduction:
The provided code implements a Contact Management System using classes in Python. It defines two classes, "Contacts" and "ContactManager," to store and manage individual contact information.

2. Classes and Functionality:
   a. Contacts Class:
      - The Contacts class is used to store individual contact information, including name, phone number, email address, and address.
      - The constructor initializes the attributes with optional values.

   b. ContactManager Class:
      - The ContactManager class is responsible for managing a list of contacts.
      - It contains methods to:
        - Add a new contact to the list.
        - View all existing contacts.
        - Search for contacts by name or phone number.
        - Delete a contact by name.

3. Method Details:
   a. add_contact:
      - Method to add a new contact to the list of contacts.
      - Accepts parameters for name, phone number, email address, and address.
      - Creates an instance of the Contacts class with the provided details and appends it to the contacts list.

   b. view_all_contacts:
      - Method to display all existing contacts.
      - If there are no contacts, a message is displayed.
      - Otherwise, it loops through the contacts list and prints each contact's details.

   c. search_contact:
      - Method to search for contacts by name or phone number.
      - Uses list comprehension to filter contacts matching the search criteria.
      - Displays matching contact details if found; otherwise, prints a message.

   d. delete_contact:
      - Method to delete a contact by name.
      - Loops through the contacts list and removes the matching contact.
      - Displays a success message if a contact is deleted; otherwise, prints a message.

4. Usage:
   - The main function creates an instance of the ContactManager class.
   - Sample contacts are added using the add_contact method.
   - Various functionalities are demonstrated, such as viewing all contacts, searching for contacts, and deleting contacts.

5. Output:
   - The program displays output in the terminal, including contact details, search results, and deletion status.

6. How to Run:
   - Copy and paste the provided code into a Python file.
   - Run the Python file using a Python interpreter.
   - Observe the output in the terminal.

7. Challenges faced during development:

   - One challenge was ensuring the user-friendly display of contact information and managing the formatting of the output.
   - Handling duplicate phone numbers required checking the existing contacts and making sure not to add duplicates. 
