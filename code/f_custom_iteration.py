class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, it):
        self.items.append(it)

    # TODO: 1. Reveal items directly
    # TODO: 2. Sorted or otherwise modified


class CartItem:
    def __init__(self, name, price):
        self.price = price
        self.name = name


cart = ShoppingCart()
cart.add_item(CartItem("guitar", 799))
cart.add_item(CartItem("cd", 19))
cart.add_item(CartItem("iPhone", 699))

# TODO: Iterate cart
