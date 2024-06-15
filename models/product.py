class Product:
    def __init__(self, id, name, price, categories=[]):
        self.id = id
        self.name = name
        self.price = price
        self.categories = categories

    def __str__(self):
        return f"Product(ID: {self.id}, Name: {self.name}, Price: {self.price}, Categories: {self.categories})"