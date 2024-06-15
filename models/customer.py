from random import randint

class Customer:
    def __init__(self, id, name, cart=[]):
        self.id = id
        self.name = name
        self.cart = cart

    def __str__(self):
        return f"Customer(ID: {self.id}, Name: {self.name}, Cart: {self.cart})"

    def add_to_cart(self, product):
        if product not in self.cart.products:
            self.cart.products.append(product)
        else:
            raise ValueError("This product is already in the cart.")

    def remove_from_cart(self, product):
        if product in self.cart.products:
            self.cart.products.remove(product)
        else:
            raise ValueError("This product is not in the cart.")