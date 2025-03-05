
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