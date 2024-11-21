


from src.controllers.order_controller.order import take_order
from src.controllers.order_controller.order import finalize_order
from src.controllers.order_controller.order import review_order
from src.controllers.order_controller.order import payment_proceed
from src.utility.error_message import ErrorMessage
from src.utility.colors import bcolors
from src.utility.validation import validate_int
from src.utility.validation import validate_name
from src.utility.get_input import get_input
from src.controllers.reservation_controller.reservation import auto_reserve


def order_system():

    err_msg = ErrorMessage()

    print(err_msg.ask_for_table_booking)
    print(f'{bcolors.OKBLUE}1 YES')
    print('2 NO')
    while True:
        option = get_input(validate_int, err_msg.choose_option, err_msg.invalid_option)
        if(option == 1 or option == 2):
            break
        elif(not option):
            print(err_msg.invalid_option)
            continue
    res = None    
    if(option == 1):
        res = auto_reserve()
        if(not res):
            print(f'{bcolors.HEADER}{err_msg.continue_booking_without_table}')
            print(f'{bcolors.OKBLUE}1 YES')
            print('2 NO')
            while True:
                action = get_input(validate_int, err_msg.choose_option, err_msg.invalid_option)
                if(action == 1):
                    break
                elif(action == 2):
                    print('thank you')
                    return

                else:
                    print(err_msg.invalid_option)
                    continue
                      
    order = take_order()
    if(not order):
        print('Thank you!')
        return
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
                    finalize_order(order, res['name'] if res else None, res['mobile_no'] if res else None)
                    break
                elif(action == 'b'):
                    order_id = finalize_order(order, res['name'] if res else None, res['mobile_no'] if res else None)
                    payment_proceed(order_id)
                    break
                    
                else:
                    print(err_msg.invalid_option)