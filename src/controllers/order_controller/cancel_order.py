
from src.database.collections.order import Order
from src.controllers.user_controller.user_state import UserState
from src.utility.validation import validate_id
from src.utility.error_message import ErrorMessage
from src.utility.get_input import get_input
from src.utility.log_error import LogError
from src.utility.colors import bcolors


def cancel_order():
    try:
        err_msg = ErrorMessage()
        ORDER = Order()
        user_state = UserState().get_state()

        order_id = get_input(validate_id, err_msg.enter_id, err_msg.invalid_id)
        if(not order_id):
            raise Exception(err_msg.invalid_id)
        
        if(user_state['role'] == 'admin'):
            for order in ORDER.orders:
                if(order['id'] == order_id):
                    if(order['status'] == 'process'):
                        order['status'] = 'cancel'
                        ORDER.save_order()
                        print(f'{bcolors.OKGREEN}{err_msg.order_cancel_success}')
                        return
                    elif(order['status']  == 'cancel'):
                        print(f'{bcolors.FAIL}{err_msg.order_already_cancel}')
                        return
                    elif(order['status'] == 'paid'):
                        print(f'{bcolors.FAIL}{err_msg.order_cannot_cancel}')
                        return
            else:
                print(err_msg.order_not_found)
    except Exception as error:
        LogError().err.exception(error)
        print(error)