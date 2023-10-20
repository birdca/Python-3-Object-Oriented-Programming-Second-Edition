class Contact:
    all_contacts: list[Contact] = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print(
            f"If this were a real system we would send '{order}' order to '{self.name}'"
        )
