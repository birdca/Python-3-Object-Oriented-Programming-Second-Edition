class ContactList(list):
    def search(self, search_filter: str) -> list:
        """
        >>> contact1 = Contact("John Doe", "john@example.com")
        >>> contact2 = Contact("Alice Smith", "alice@example.com")
        >>> contact3 = Contact("Bob Johnson", "bob@example.com")

        >>> matches = Contact.all_contacts.search("John")
        >>> len(matches)
        2
        >>> matches[0].name
        'John Doe'
        >>> matches[1].name
        'Bob Johnson'
        """
        matching_contacts = []
        for contact in self:
            if search_filter in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts: list = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        """
        >>> supplier = Supplier("Supplier1", "supplier@example.com")
        >>> supplier.order("Widgets")
        If this were a real system we would send 'Widgets' order to 'Supplier1'
        """
        print(
            f"If this were a real system we would send '{order}' order to '{self.name}'"
        )
