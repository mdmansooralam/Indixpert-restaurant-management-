


from src.controllers.order_controller.order import take_order
from src.controllers.order_controller.order import finalize_order
from src.controllers.order_controller.order import review_order
from src.controllers.order_controller.order import payment_proceed
from src.utility.error_message import ErrorMessage

from src.utility.validation import validate_name
from src.utility.get_input import get_input


def order_system():
    order = take_order()
    err_msg = ErrorMessage()
    while True:
            print('A. Add')
            print('R. Review')
            print('S. Save')
            print('B. Billing')
            print('Q. Quit')
            action = get_input(validate_name, err_msg.choose_option, err_msg.invalid_option)
            if(not action):
                print(err_msg.invalid_option)
                break
            else:
                if(action == 'q'):
                    print('Thank You !')
                    break

                elif(action == 'a'):
                    order.extend(take_order())

                elif(action == 'r'):
                    review_order(order)

                elif(action == 's'):
                    finalize_order(order)
                    break
                elif(action == 'b'):
                    order_id = finalize_order(order)
                    payment_proceed(order_id)
                    break
                    
                else:
                    print(err_msg.invalid_option)