class Product:
    _name = None
    _price = 0.0

    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def get_price(self):
        return self._name

    def __str__(self):
        return "%s @ %s" % (self._name, self._price)