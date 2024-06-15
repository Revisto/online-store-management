from services.product_service import ProductService
from services.customer_service import CustomerService
from services.order_service import OrderService
from services.payment_service import PaymentService
from utils.ui import UI

def main():
    product_service = ProductService()
    customer_service = CustomerService()
    order_service = OrderService()
    payment_service = PaymentService()

    ui = UI(customer_service, product_service, order_service, payment_service)

    ui.start()

if __name__ == "__main__":
    main()