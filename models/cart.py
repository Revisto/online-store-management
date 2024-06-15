class Cart:
    def __init__(self, products=None):
        self.products = products if products else []

    def __str__(self):
        return f"Cart(Products: {[product.name for product in self.products]}, Total Price: {self.calculate_total_price()})"

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
        else:
            raise ValueError("This product is already in the cart.")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("This product is not in the cart.")

    def calculate_total_price(self):
        return sum(product.price for product in self.products)