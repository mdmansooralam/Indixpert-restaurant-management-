


from src.database.collections.order import Order
from src.utility.check_order import check_order
from src.controllers.payment_gateway_controller.payment_gateway import pay




def payment_proceed(order_id):
    try:

        if(check_order(order_id)):
            ORDER = Order()
            for order in ORDER.orders:
                if(order['id'] == order_id):
                    if(order['status'] == 'process'):
                        is_paid = pay(order_id)
                        if(is_paid == 'success'):
                            order['status'] = 'paid'
                            ORDER.save_order()
                            print('payment successful')
                    else:
                        print('Order not in process or paid')
        else:
            print('order not found')
    except Exception as error:
        print(error)

