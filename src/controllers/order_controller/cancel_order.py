
from src.database.collections.order import Order
from src.controllers.user_controller.user_state import UserState
from src.utility.validation import validate_id
from src.utility.error_message import ErrorMessage


def cancel_order():
    try:
        err_msg = ErrorMessage()
        ORDER = Order()
        user_state = UserState().get_state()

        order_id = validate_id(input('Enter Order Id : '))
        if(not order_id):
            raise Exception(err_msg.invalid_id)
        
        if(user_state['role'] == 'admin'):
            for order in ORDER.orders:
                if(order['id'] == order_id):
                    if(order['status'] == 'process'):
                        order['status'] = 'cancel'
                        ORDER.save_order()
                        print('Order cancel successful ')
                        return
                    elif(order['status']  == 'cancel'):
                        print('order already cancelled')
                        return
                    elif(order['status'] == 'paid'):
                        print('complete order can not be cancel')
                        return
            else:
                print('order not found')
    except Exception as error:
        print(error)