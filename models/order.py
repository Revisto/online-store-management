class Order:
    def __init__(self, id, customer_id, products, total_price, status):
        self.id = id
        self.customer_id = customer_id
        self.products = products
        self.total_price = total_price
        self.status = status

    def __str__(self):
        return f"Order(ID: {self.id}, Customer Id: {self.customer_id}, Products: {[product_id for product_id in self.products]}, Total Price: {self.total_price}, Status: {self.status})"