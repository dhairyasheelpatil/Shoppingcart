class Address:
    _streetNumber = None
    _streetNumber2 = None
    _street = None
    _city = None
    _zipcode = None
    _country = None

    def __init__(self, streetNumber, street, city, zipcode, country):
        self._streetNumber = streetNumber
        self._street = street
        self._city = city
        self._zipcode = zipcode
        self._country = country

    def __init__(self, streetNumber, streetNumber2, street, city, zipcode, country):
        self._streetNumber = streetNumber
        self._streetNumber2 = streetNumber2
        self._street = street
        self._city = city
        self._zipcode = zipcode
        self._country = country

    def __str__(self):
        return "%s %s %s %s %s %s" % (self._streetNumber, self._streetNumber2, self._street, self._city, self._zipcode, self._country )