
from models.payment import Payment
from utils.file_handler import FileHandler
import secrets

class PaymentService:
    def __init__(self):
        self.file_handler = FileHandler('payments.txt')
        self.payments = self.load_payments()

    def load_payments(self):
        data = self.file_handler.read()
        return [Payment(**payment) for payment in data]

    def save_payments(self):
        data = [payment.__dict__ for payment in self.payments]
        self.file_handler.write(data)

    def add_payment(self, customer, amount, method):
        payment_id = secrets.SystemRandom().randint(1, 999)
        payment = Payment(payment_id, customer.id, amount, method, "done")
        self.payments.append(payment)
        self.save_payments()
