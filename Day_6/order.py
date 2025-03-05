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