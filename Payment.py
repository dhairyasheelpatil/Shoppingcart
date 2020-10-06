import Address
class Payment:
    _accountNumber = None
    _name = None
    _address = None

    def __init__(self, accountNumber, name, address: Address):
        self._accountNumber = accountNumber
        self._name = name
        self._address = address

    def get_accountNumber(self):
        return self._accountNumber

    def get_billingAddress(self):
        return self._address

    def get_name(self):
        return self._name

    def update(self, accountNumber, name, address: Address):
        self._accountNumber = accountNumber
        self._name = name
        self._address = address

    def __str__(self):
        return "Payment: x%s" %  self.get_accountNumber()[-4:]