class OrderItems:
    def init(self, order_id, item_id, product_id, quantity, list_price, discount):
        self.order_id = order_id
        self.item_id = item_id
        self.product_id = product_id
        self.quantity = quantity
        self.list_price = list_price
        self.discount = discount

    def display_info(self):
        print(f"Order ID: {self.order_id}, Item ID: {self.item_id}")
        print(f"Product ID: {self.product_id}, Quantity: {self.quantity}")
        print(f"List Price: {self.list_price}, Discount: {self.discount}")