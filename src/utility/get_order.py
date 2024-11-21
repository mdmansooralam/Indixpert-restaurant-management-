

from src.database.collections.order import Order

def get_order(id):
    orders = Order().orders

    order_found = False
    for order in orders:
        if(order['id'] == id):
            order_found = True
            return order
    if(not order_found):
        return False