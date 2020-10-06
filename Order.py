import abc


class OrderContext:
    _order_id = None
    _shoppingCart = None
    _state = None

    def __init__(self, shoppingCart):
        self._shopping_cart = shoppingCart

    def set_order_id(self, order_id):
        self._order_id = order_id

    def get_order_id(self):
        return self._order_id

    def get_shopping_cart(self):
        return self._shopping_cart

    def set_state(self, state):
        print("Context: New State: %s" % type(state).__name__)
        self._state = state
        self._state.set_context(self)


    def get_state(self):
        print('Current Context State: %s' % type(self._state).__name__)

        return self._state

    def proceed(self):
        self._state.next()

    def go_back(self):
        self._state.prev()

    def renderView(self):
        self._state.display()


class OrderState(metaclass=abc.ABCMeta):
    _context = None
    def get_context(self):
        return self._context

    def set_context(self, context):
        self._context = context

    @abc.abstractmethod
    def prev(self):
        pass

    @abc.abstractmethod
    def next(self):
        pass

    @abc.abstractmethod
    def display(self):
        pass

class OrderCheckoutState(OrderState):
    def prev(self):
        print("Nothing to go back to....")

    def next(self):
        try:
            print("Process with Checkout....")
            self._context.set_state(OrderPaymentState())
        except:
            self._context.set_state(OrderCheckoutErrorState())
    def display(self):
        print("Begin Checkout....")

class OrderCheckoutErrorState(OrderCheckoutState):
    def prev(self):
        print("Go back to the Checkout State")
        self._context.set_state(OrderCheckoutState())
    def next(self):
        print("Something when wrong with Checkout process. Go back to checkout state")
        self._context.set_state(OrderCheckoutState())
    def display(self):
        print("Display Checkout Error....")


class OrderPaymentState(OrderState):
    def prev(self):
        self._context.set_state(OrderCheckoutState())

    def next(self):
        try:
            print("Processing Payment")
            #TODO Process Payment
            self._context.set_state(OrderConfirmationState())
        except:
            self._context.set_state(OrderPaymentErrorState())

    def display(self):
        print("Display Payment Page....")

class OrderPaymentErrorState(OrderPaymentState):
    def prev(self):
        self._context.set_state(OrderCheckoutState())

    def next(self):
        print("Payment Error. Go back to Payment State to retry....")
        self._context.set_state(OrderPaymentState())

    def display(self):
        print("Display Payment Error Page....")

class OrderConfirmationState(OrderState):
    def prev(self):
        print("Too Late to go back, since the order has been placed")

    def next(self):
        print("There is no next step.....")

    def display(self):
        context = self.get_context()
        user = context.get_shopping_cart().get_session().get_user()
        print("Order has been placed. Order #: %s for %s" % (context.get_order_id(), user) )
