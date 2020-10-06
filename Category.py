import Product

class Category:
    _name = None
    _products = []

    def __init__(self, name):
        self._name = name

    def add_product(self, product: Product):
        self._products.append(product)

    def remove_product(self, product: Product):
        self._products.remove(product)

    def get_name(self):
        return self._name

    def get_products(self):
        return self._products
