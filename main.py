from User import User
from Address import Address
from Product import Product
from Category import Category
from ShoppingCart import ShoppingCart, RecommendationEngineA, RecommendationEngineB
from Payment import Payment
from Session import Session
from Order import OrderContext, OrderCheckoutState

if __name__ == "__main__":
    # New User
    user = User("John", "Doe", "JDoe@example.com")
    address = Address("123", "Main St", "San Mateo", "CA", "94401", "USA")
    user.add_address(address)
    user.add_payment(Payment("1234-5678-1234-1234", "Chase", address))

    # New Categories
    pet_cat = Category("Pet")
    home_cat = Category("Home")

    # New Products
    pet_cat.add_product(Product("Scratch Post", 34.99))
    pet_cat.add_product(Product("Litter Box", 10.99))
    pet_cat.add_product(Product("Wet Food", 1.99))

    home_cat.add_product(Product("Towel", 5.98))
    home_cat.add_product(Product("Utensil", 12.49))
    home_cat.add_product(Product("Sofa", 1099.48))

    #New Session
    session = Session(user)

    #Shopping Cart

    shoppingCart = ShoppingCart(session)
    shoppingCart.attach(RecommendationA())
    item1 = pet_cat.get_products()[0]
    item2 = home_cat.get_products()[2]
    shoppingCart.add_item(item1)
    shoppingCart.add_item(item2)


    # Checkout Process
    context = OrderContext(shoppingCart)
    context.set_order_id('12345678')
    context.set_state(OrderCheckoutState())
    context.proceed()
    context.renderView()

    context.proceed()
    context.renderView()