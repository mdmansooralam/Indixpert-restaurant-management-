

from src.utility.validation import validate_int
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.dashboard.UI.order_ui.order_system import order_system
from src.controllers.order_controller.order import get_unpaid_order
from src.controllers.order_controller.update_order import update_order 
from src.controllers.order_controller.cancel_order import cancel_order
from src.controllers.order_controller.order import get_all_order, get_order_details
from src.utility.error_message import ErrorMessage
from src.controllers.user_controller.user_state import UserState


def order_page():
    err_msg = ErrorMessage()
    user_state = UserState().get_state()

    if(user_state['role'] == 'staff'):
        while True:
            print('*****************Order Page ***********************')
            print('1 CREATE ORDER')
            print('2 UPDATE ORDER')
            print('3 VIEW ORDER IN PROCESS')
            print('4 BACK')


            choice = validate_int(input("please choose a option : "))
            if(not choice):
                print(err_msg.invalid_option)
                continue
            elif(choice == 1):
                order_system()
                if(ask_for_dashboard("Back")):
                    continue
                else:
                    break
            elif(choice == 2):
                update_order()
                if(ask_for_dashboard("Back")):
                    continue
                else:
                    break
            elif(choice == 3):
                get_unpaid_order()
                if(ask_for_dashboard("Back")):
                    continue
                else:
                    break
            elif(choice == 4):
                break
            else:
                print('please choose a valid option ')
                if(ask_for_dashboard()):
                    continue
                else:
                    break

    elif(user_state['role'] == 'admin'):
        while True:
            print('*****************Order Page ***********************')
            print('1 CANCEL ORDER')
            print('2 VIEW ORDER DETAILS')
            print('3 VIEW ALL ORDER')
            print('4 BACK')


            choice = validate_int(input("please choose a option : "))
            if(not choice):
                print(err_msg.invalid_option)
                continue
            elif(choice == 1):
                cancel_order()
                if(ask_for_dashboard("Back")):
                    continue
                else:
                    break
            elif(choice == 2):
                get_order_details()
                if(ask_for_dashboard("Back")):
                    continue
                else:
                    break
            elif(choice == 3):
                get_all_order()
                if(ask_for_dashboard("Back")):
                    continue
                else:
                    break
            elif(choice == 4):
                break
            else:
                print('please choose a valid option ')
                if(ask_for_dashboard()):
                    continue
                else:
                    break

