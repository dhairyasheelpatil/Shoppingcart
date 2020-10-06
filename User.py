import Address, Payment

class User:
    _firstName = ""
    _lastName = ""
    _email = ""
    _payments = []
    _addresses = []

    def __init__(self):
        pass

    def __init__(self, firstName, lastName, email):
        self._firstName = firstName
        self._lastName = lastName
        self._email = email

    def get_email(self) -> str:
        return self._email

    def set_email(self, email) -> None:
        self._email = email

    def get_firstName(self) -> str:
        return self._firstName

    def set_firstName(self, firstName) -> None:
        self._firstName = firstName

    def get_lastName(self) -> str:
        return self._lastName

    def set_lastName(self, firstName) -> None:
        self._firstName = firstName

    def add_payment(self, payment: Payment) -> None:
        self._payments.append(payment)

    def remove_payment(self, payment: Payment) -> None:
        self._payments.remove(payment)

    def get_payments_list(self):
        return self._payments

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)

    def remove_address(self, address: Address) -> None:
        self._addresses.remove(address)

    def get_address_list(self):
        return self._addresses

    def __str__(self):
        return "%s %s ( %s )" % (self.get_firstName(), self.get_lastName(), self.get_email())