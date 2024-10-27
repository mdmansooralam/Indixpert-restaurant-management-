





from src.database.collections.order import Order
from src.utility.check_order import check_order




def payment_proceed(order_id):

    if(check_order(order_id)):
        ORDER = Order()
        for order in ORDER.orders:
            if(order['id'] == order_id):
                if(order['status'] == 'process'):
                    order['status'] = 'complete'
                    ORDER.save_order()
                    print('payment proceed successful .')
                elif(order['status'] == 'complete'):
                    print('order already completed')
    else:
        print('order not found')

