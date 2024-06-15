from random import randint

from models.customer import Customer
from services.product_service import ProductService
from services.order_service import OrderService
from services.base_service import BaseService

class CustomerService(BaseService):
    def __init__(self):
        super().__init__('customers.txt')
        self.customers = self.load_data(Customer)

    def load_customers(self):
        data = self.file_handler.read()
        return [Customer(**customer) for customer in data]

    def save_customers(self):
        data = [customer.__dict__ for customer in self.customers]
        self.file_handler.write(data)

    def add_customer(self, name, cart=[]):
        customer_id = randint(1, 999)
        customer = Customer(customer_id, name, cart)
        self.customers.append(customer)
        self.save_customers()

    def remove_customer(self, id):
        customer = self.get_customer(id)
        if customer:
            self.customers.remove(customer)
            self.save_customers()

    def get_customer(self, name):
        for customer in self.customers:
            if customer.name == name:
                return customer
        return None
    
    def get_customer_by_id(self, id):
        for customer in self.customers:
            if customer.id == id:
                return customer
        return None

    def update_customer(self, id, name=None, address=None, cart=[]):
        customer = self.get_customer_by_id(id)
        if customer:
            if name:
                customer.name = name
            if address:
                customer.address = address
            if cart:
                customer.cart = cart
            self.save_customers()

    def add_product_to_cart(self, customer, product_id):
        customer.cart.append(product_id)
        self.save_customers()

    def delete_product_from_cart(self, customer, product_id):
        customer.cart.remove(product_id)
        self.save_customers()

    def list_products_in_cart(self, customer):
        cart = []
        for product in customer.cart:
            cart.append(ProductService().get_product(product))
        return cart
    
    def get_cart_total(self, customer):
        total = 0
        for product in customer.cart:
            total += ProductService().get_product(product).price
        return total
    
    def clear_cart(self, customer):
        customer.cart = []
        self.save_customers()

    def get_orders(self, customer):
        orders = []
        for order in OrderService().orders:
            if int(order.customer_id) == int(customer.id):
                orders.append(order)
        return orders