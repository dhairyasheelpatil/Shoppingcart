from abc import ABC, abstractmethod
import Session
import Product

class Cart(ABC):

    @abstractmethod
    def attach(self, recommendation) -> None:
        pass

    @abstractmethod
    def detach(self, recommendation) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class ShoppingCart(Cart):

    _session = None

    _session_recommendations = []

    _items = []

    def __init__(self, session: Session):
        self._session = session

    def attach(self, recommendation) -> None:
        print(f"\nShoppingCart: Attached {self._session} session recommendation.")
        self._session_recommendations.append(recommendation)

    def detach(self, recommendation) -> None:
        self._session_recommendations.remove(recommendation)

    def notify(self) -> None:
        print("ShoppingCart: Notifying recommendation engine")
        for recommendation_engine in self._session_recommendations:
            recommendation_engine.update(self)

    def add_item(self, item: Product) -> None:
        print(f"ShoppingCart: Item from {item} category got added to {self._session}'s cart.")
        self._items.append(item)
        self.notify()

    def remove_item(self, item: Product) -> None:
        print(f"ShoppingCart: Item from {item} category got removed from {self._session}'s cart.")
        self._items.remove(item)

    def subtotal(self) -> None:
        print(f"ShoppingCart: Item from {self._category} category got added to {self._session.get_user()}'s cart.")
        self.notify()

    def get_session(self):
        return self._session

class Recommendation(ABC):

    @abstractmethod
    def update(self, cart: Cart) -> None:
        pass


class RecommendationEngineA(Recommendation):
    def update(self, cart: Cart) -> None:
        print("%s : might also like ???????" % cart.get_session().get_user())



class RecommendationEngineB(Recommendation):
    def update(self, cart: Cart) -> None:
        if cart._category == "Fruit":
            print("UserB: You might also like mango")
        elif cart._category == "Electronics":
            print("UserB: You might also like laptop")
        elif cart._category == "Clothes":
            print("UserB: You might also like shirts")
