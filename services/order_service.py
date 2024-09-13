
from models.order import Order
from utils.file_handler import FileHandler
import secrets

class OrderService:
    def __init__(self):
        self.file_handler = FileHandler('orders.txt')
        self.orders = self.load_orders()

    def load_orders(self):
        data = self.file_handler.read()
        return [Order(**order) for order in data]

    def save_orders(self):
        data = [order.__dict__ for order in self.orders]
        self.file_handler.write(data)

    def place_order(self, customer, total_price):
        order_id = secrets.SystemRandom().randint(1, 999)
        order = Order(order_id, customer.id, customer.cart, total_price, "done")
        self.orders.append(order)
        self.save_orders()
