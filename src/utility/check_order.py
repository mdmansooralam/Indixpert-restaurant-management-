

from src.database.collections.order import Order

def check_order(id):
    orders = Order().orders

    order_found = False
    for order in orders:
        if(order['id'] == id):
            order_found = True
            return True
    else:
        if(not order_found):
            return False