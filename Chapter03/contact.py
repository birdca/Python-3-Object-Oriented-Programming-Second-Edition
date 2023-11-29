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


class Friend(Contact):
    def __init__(self, name, email, phone):
        """
        A class representing a friend contact.

        This class inherits from the Contact class and adds a phone number attribute.

        Example:
        >>> friend = Friend("John", "john@example.com", "123-456-7890")
        >>> friend.name
        'John'
        >>> friend.email
        'john@example.com'
        >>> friend.phone
        '123-456-7890'
        """
        super().__init__(name, email)
        self.phone = phone


class LongNameDict(dict):
    def longest_key(self):
        """
        >>> longkeys = LongNameDict()
        >>> longkeys['hello'] = 1
        >>> longkeys['longest yet'] = 5
        >>> longkeys['hello2'] = 'world'
        >>> longkeys.longest_key()
        'longest yet'
        """
        longest_key = ""
        for key in self:
            if len(key) > len(longest_key):
                longest_key = key

        return longest_key


class MailSender:
    def send_mail(self, context):
        print(f"Send '{context}' to '{self.email}'")


class EmailableContact(Contact, MailSender):
    """
    >>> e = EmailableContact("John Smith", "jsmith@example.net")
    >>> e.send_mail("Hello, test e-mail here")
    Send 'Hello, test e-mail here' to 'jsmith@example.net'
    """
