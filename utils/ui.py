class UI:
    def __init__(self, customer_service, product_service, order_service, payment_service):
        self.customer_service = customer_service
        self.product_service = product_service
        self.order_service = order_service
        self.payment_service = payment_service

    def start(self):
        print("Are you a superadmin or a customer? ")
        print("1. Superadmin")
        print("2. Customer")
        user_type = input("Choose an option: ")
        if user_type.lower() == "1":
            self.superadmin_interface()
        elif user_type.lower() == "2":
            self.customer_interface()
        else:
            print("Invalid choice. Please choose a number between 1 and 2.")

    def superadmin_interface(self):
        while True:
            print("1. List products")
            print("2. List orders")
            print("3. List payments")
            print("4. Add product")
            print("5. Update product")
            print("6. Delete product")
            print("7. Exit")
            choice = input("Choose an option: ")
            print("-" * 50)
            if choice == "1":
                self.list_products()
            elif choice == "2":
                self.list_orders()
            elif choice == "3":
                self.list_payments()
            elif choice == "4":
                self.add_product()
            elif choice == "5":
                self.update_product()
            elif choice == "6":
                self.delete_product()
            elif choice == "7":
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 7.")
            print("-" * 50)

    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        categories = input("Enter product categories (comma-separated): ").split(",")
        categories = [category.strip() for category in categories]
        self.product_service.add_product(name, price, categories)

    def update_product(self):
        products = self.product_service.load_products()
        for product in products:
            print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Categories: {product.categories}")
        
        id = int(input("Enter product ID: "))
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        categories = input("Enter product categories (comma-separated): ").split(",")
        categories = [category.strip() for category in categories]

        if name == "":
            name = None
        if price == "":
            price = None
        if categories == "":
            categories = None
        self.product_service.update_product(id, name, price, categories)
        print(f"Product with ID {id} updated.")

    def delete_product(self):
        products = self.product_service.load_products()
        for product in products:
            print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Categories: {product.categories}")
        
        id = int(input("Enter product ID: "))
        self.product_service.remove_product(id)
        print(f"Product with ID {id} deleted.")

    def customer_interface(self):
        name = input("Enter your name: ")
        customer = self.customer_service.get_customer(name)
        if not customer:
            create = input("No customer found. Would you like to create a new customer? (yes/no) ")
            if create.lower() == "yes":
                self.customer_service.add_customer(name)
                print(f"Customer {name} created.")
            else:
                return
        while True:
            print("1. Add product to cart")
            print("2. Delete product from cart")
            print("3. List products in cart")
            print("4. Search for products by category")
            print("5. Pay for products in cart")
            print("6. See previous orders")
            print("7. Exit")
            choice = input("Choose an option: ")
            print("-" * 50)
            if choice == "1":
                self.add_product_to_cart(customer)
            elif choice == "2":
                self.delete_product_from_cart(customer)
            elif choice == "3":
                self.list_products_in_cart(customer)
            elif choice == "4":
                self.search_products_by_category()
            elif choice == "5":
                self.make_payment(customer)
            elif choice == "6":
                self.get_orders(customer)
            elif choice == "7":
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 7.")
            print("-" * 50)

    def get_orders(self, customer):
        orders = self.customer_service.get_orders(customer)
        for order in orders:
            print(order)

    def search_products_by_category(self):
        all_categories = []
        products = self.product_service.load_products()
        for product in products:
            all_categories.extend(product.categories)
        all_categories = list(set(all_categories))
        for i, category in enumerate(all_categories):
            print(f"{i + 1}. {category}")
        choice = int(input("Choose a category: "))
        category = all_categories[choice - 1]
        for product in products:
            if category in product.categories:
                print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Categories: {product.categories}")
        

    def add_product_to_cart(self, customer):
        products = self.product_service.load_products()
        for product in products:
            print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}")
        product_id = input("Enter the product ID to add to the cart: ")
        if not self.product_service.get_product(product_id):
            print("Invalid product ID.")
            return
        self.customer_service.add_product_to_cart(customer, product_id)

    def delete_product_from_cart(self, customer):
        product_id = input("Enter the product ID to delete from the cart: ")
        self.customer_service.delete_product_from_cart(customer, product_id)

    def list_products_in_cart(self, customer):
        products = self.customer_service.list_products_in_cart(customer)
        if products == []:
            print("Cart is empty.")
        else:
            for product in products:
                print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}")

    def make_payment(self, customer):
        amount = self.customer_service.get_cart_total(customer)
        confirm = input(f"Total amount to pay: {amount}. Confirm payment? (yes/no) ")
        if confirm.lower() == "yes":
            self.order_service.place_order(customer, amount)
            method = input("Enter payment method (cash/card): ")
            self.payment_service.add_payment(customer, amount, method)
            self.customer_service.clear_cart(customer)
            print("Payment successful.")
        else:
            print("Payment cancelled.")

    def list_products(self):
        products = self.product_service.load_products()
        for product in products:
            print(product)

    def list_orders(self):
        orders = self.order_service.load_orders()
        for order in orders:
            print(order)

    def list_payments(self):
        payments = self.payment_service.load_payments()
        for payment in payments:
            print(payment)