class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, it):
        self.items.append(it)

    # def __iter__(self):
    #     return self.items.__iter__()

    def __iter__(self):
        for i in sorted(self.items, key=lambda x: -x.price):
            yield i


class CartItem:
    def __init__(self, name, price):
        self.price = price
        self.name = name


cart = ShoppingCart()
cart.add_item(CartItem("guitar", 799))
cart.add_item(CartItem("cd", 19))
cart.add_item(CartItem("iPhone", 699))

for item in cart:
    print(" * ${} {}".format(item.price, item.name))
