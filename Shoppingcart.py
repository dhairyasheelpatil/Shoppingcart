from __future__ import annotations
from abc import ABC, abstractmethod
import random
import abc
from typing import List


class Category(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def category(self):
        self._category.category()


class Fruit(Category):
    def category(self):
        print("Fruit!!")


class Clothes(Category):
    def category(self):
        print("Clothes!")


class Electronics(Category):
    def category(self):
        print("Electronics!")


class Item(object):

  def __init__(self, category):
      self._category = category

  def category(self):
      self._category.category()


class Apple(Item):
    def __init__(self):
        super(Apple, self).__init__(fruit)

    def price(self):
        price = 3
        return price


class Phone(Item):
    def __init__(self):
        super(Phone, self).__init__(electronics)

    def price(self):
        price = 1800
        return price


class Jeans(Item):
    def __init__(self):
        super(Jeans, self).__init__(clothes)

    def price(self):
        price = 30
        return price


class Cart(ABC):

    @abstractmethod
    def attach(self, recommendation: Recommendation) -> None:
        pass

    @abstractmethod
    def detach(self, recommendation: Recommendation) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ShoppingCart(Cart):

    _category: str = None
    _user: str = None

    _session_recommendations: List[Recommendation] = []

    def attach(self, recommendation: Recommendation, user) -> None:
        print(f"\nShoppingCart: Attached {user}'s session recommendation.")
        self._session_recommendations.append(recommendation)

    def detach(self, recommendation: Recommendation) -> None:
        self._session_recommendations.remove(recommendation)

    def notify(self) -> None:

        print("ShoppingCart: Notifying recommendation engine")
        for recommendation_engine in self._session_recommendations:
            recommendation_engine.update(self)

    def add_item(self, user) -> None:

        print("ShoppingCart: Checking items in the cart.")
        self._category = random.choice(["Electronics", "Fruit", "Clothes"])

        print(f"ShoppingCart: Item from {self._category} category got added to {user}'s cart.")
        self.notify()

    def subtotal(self, user) -> None:

        # print("ShoppingCart: calculating pa.")
        self._category = random.choice(["Electronics", "Fruit", "Clothes"])

        print(f"ShoppingCart: Item from {self._category} category got added to {user}'s cart.")
        self.notify()



class Recommendation(ABC):

    @abstractmethod
    def update(self, cart: Cart) -> None:
        pass


class RecommendationUserA(Recommendation):
    def update(self, cart: Cart) -> None:
        if cart._category == "Electronics" and 'A' in cart._user:
            print("UserA: You might also like laptop")



class RecommendationUserB(Recommendation):
    def update(self, cart: Cart) -> None:
        if cart._category == "Fruit":
            print("UserB: You might also like mango")
        elif cart._category == "Electronics":
            print("UserB: You might also like laptop")
        elif cart._category == "Clothes":
            print("UserB: You might also like shirts")



if __name__ == "__main__":

    cart = ShoppingCart()

    user_a = RecommendationUserA()
    user_b = RecommendationUserB()

    cart.attach(user_a, "UserA")
    cart.add_item("UserA")

    cart.attach(user_b, "UserB")
    cart.add_item("UserB")

    cart.detach(user_a)


    fruit = Fruit()
    electronics = Electronics()
    clothes = Clothes()
    # item = Apple()
    # item.category()
    # print(item.price())
    #
    # item = Phone()
    # item.category()
    # print(item.price())
    #
    #
    # item = Jeans()
    # item.category()
    # print(item.price())

    # user_a_items = [Apple(), Phone(), Jeans()]
    # user_b_items = [Apple(), Jeans()]
    #
    # for item in user_a_items:
    #     print(item.price())


