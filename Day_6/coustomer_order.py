
class Customer:
    def __init__(self, customer_id, first_name, last_name, phone, email, street, city, state, zip_code):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.customer_details=[]
        
        def add_customer_details(self, customer_detail):
            self.customer_details.append(customer_detail)

    def __str__(self):
        return f"Customer {self.customer_id}: {self.first_name} {self.last_name}, {self.phone}, {self.email}, {self.street}, {self.city}, {self.state}, {self.zip_code}"


class Order:
    def __init__(self, order_id, customer, order_status, order_date, required_date, shipped_date, store_id, staff_id):
        self.order_id = order_id
        self.customer = customer  
        self.order_status = order_status
        self.order_date = order_date
        self.required_date = required_date
        self.shipped_date = shipped_date
        self.store_id = store_id
        self.staff_id = staff_id
        self.order_details = []  # Li

    def add_order_detail(self, order_detail):
        self.order_details.append(order_detail)

    def __str__(self):
        return f"Order {self.order_id}: Customer {self.customer.customer_id}, Status: {self.order_status}, Items: {len(self.order_details)}"


class OrderDetail:
    def __init__(self, item_id, product_id, quantity, list_price, discount):
        self.item_id = item_id
        self.product_id = product_id
        self.quantity = quantity
        self.list_price = list_price
        self.discount = discount
        self.add_order

    def __str__(self):
        return f"Item {self.item_id}: Product {self.product_id}, Quantity: {self.quantity}, Price: {self.list_price}, Discount: {self.discount}"


# Example Usage
if __name__ == "__main__":
    # Creating a customer
    customer1 = Customer(1, "John", "Doe", "1234567890", "john@example.com", "123 Main St", "New York", "NY", "10001")
    
    # Creating an order for the customer
    order1 = Order(101, customer1, "Shipped", "2025-01-01", "2025-01-05", "2025-01-03", 1, 1001)
    
    # Adding order details
    order1.add_order_detail(OrderDetail(1, 501, 2, 20.00, 0.1))
    order1.add_order_detail(OrderDetail(2, 502, 1, 50.00, 0.05))
    
    # Displaying customer and order details
    print(customer1)
    print(order1)
    for detail in order1.order_details:
        print(detail)