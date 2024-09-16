
from models.product import Product
from utils.file_handler import FileHandler
import secrets

class ProductService:
    def __init__(self):
        self.file_handler = FileHandler("products.txt")
        self.products = self.load_products()

    def load_products(self):
        data = self.file_handler.read()
        return [Product(**product) for product in data]

    def save_products(self):
        data = [product.__dict__ for product in self.products]
        self.file_handler.write(data)

    def add_product(self, name, price, categories):
        product = Product(secrets.SystemRandom().randint(1, 999), name, price, categories)
        self.products.append(product)
        self.save_products()

    def remove_product(self, id):
        product = self.get_product(id)
        if product:
            self.products.remove(product)
            self.save_products()

    def get_product(self, id):
        for product in self.products:
            if int(product.id) == int(id):
                return product
        return None

    def update_product(self, id, name=None, price=None, categories=None):
        product = self.get_product(id)
        if product:
            if name:
                product.name = name
            if price:
                product.price = float(price)
            if categories:
                product.categories = categories
            self.save_products()
