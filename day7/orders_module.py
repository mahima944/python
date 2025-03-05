class Order:
    def __init__(self, order_id, customer_id, status, order_date, ship_date, delivery_date, payment_id, shipping_id):
        self.order_id = order_id
        self.customer_id = customer_id
        self.status = status
        self.order_date = order_date
        self.ship_date = ship_date
        self.delivery_date = delivery_date
        self.payment_id = payment_id
        self.shipping_id = shipping_id

    def display_info(self):
        print(f"Order ID: {self.order_id}, Status: {self.status}, Order Date: {self.order_date}, Ship Date: {self.ship_date}")
