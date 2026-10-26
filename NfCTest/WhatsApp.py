class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show_profile(self):
        print("\nName:", self.name)
        print("Phone:", self.phone)


class Message:
    def __init__(self, sender, receiver, text):
        self.sender = sender
        self.receiver = receiver
        self.text = text

    def show_message(self):
        print(self.sender, ":", self.text)


class WhatsApp(User):
    def __init__(self, name, phone):
        super().__init__(name, phone)
        self.contacts = []
        self.messages = []

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter contact phone: ")

        contact = User(name, phone)
        self.contacts.append(contact)

        print("Contact added successfully!")

    def show_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts available.")
        else:
            print("\n--- Contact List ---")
            for contact in self.contacts:
                print(contact.name, "-", contact.phone)

    def send_message(self):
        receiver = input("Enter receiver name: ")
        text = input("Enter your message: ")

        found = False

        for contact in self.contacts:
            if contact.name == receiver:
                message = Message(self.name, receiver, text)
                self.messages.append(message)
                print("Message sent successfully!")
                found = True
                break

        if not found:
            print("Contact not found!")

    def show_chats(self):
        if len(self.messages) == 0:
            print("No messages available.")
        else:
            print("\n--- Chat History ---")
            for message in self.messages:
                message.show_message()

    def menu(self):
        while True:
            print("\n===== WHATSAPP CONSOLE =====")
            print("1. Show Profile")
            print("2. Add Contact")
            print("3. Show Contacts")
            print("4. Send Message")
            print("5. Show Chat History")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.show_profile()

            elif choice == "2":
                self.add_contact()

            elif choice == "3":
                self.show_contacts()

            elif choice == "4":
                self.send_message()

            elif choice == "5":
                self.show_chats()

            elif choice == "6":
                print("Thank you for using WhatsApp!")
                break

            else:
                print("Invalid choice!")


name = input("Enter your name: ")
phone = input("Enter your phone number: ")

app = WhatsApp(name, phone)
app.menu()
