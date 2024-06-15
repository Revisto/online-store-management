class Payment:
    def __init__(self, id, customer_id, amount, method, status):
        self.id = id
        self.customer_id = customer_id
        self.amount = amount
        self.method = method
        self.status = status

    def __str__(self):
        return f"Payment(ID: {self.id}, Customer Id: {self.customer_id}, Amount: {self.amount}, Method: {self.method}, Status: {self.status})"

    def update_status(self, new_status):
        self.status = new_status