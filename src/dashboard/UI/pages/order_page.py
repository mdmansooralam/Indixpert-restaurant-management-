

from src.utility.validation import validate_int
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.dashboard.UI.order_ui.order_system import order_system
from src.controllers.order_controller.order_report import get_unpaid_order
from src.controllers.order_controller.order import update_order 
from src.controllers.order_controller.cancel_order import cancel_order
from src.controllers.order_controller.order_report import get_all_order, get_order_details, today_order
from src.utility.error_message import ErrorMessage
from src.controllers.user_controller.user_state import UserState
from src.utility.get_input import get_input
from src.utility.colors import bcolors


def order_page():
    err_msg = ErrorMessage()
    user_state = UserState().get_state()

    if(user_state['role'] == 'staff'):
        while True:
            print(f'{bcolors.HEADER}*****************Order Page ***********************')
            print(f'{bcolors.OKBLUE}1 CREATE ORDER')
            print('2 UPDATE ORDER')
            print('3 VIEW ORDER IN PROCESS')
            print('4 VIEW TODAY ORDER')
            print('5 BACK')


            choice = get_input(validate_int, err_msg.choose_option, err_msg.invalid_option)
            if(not choice):
                print(f'{bcolors.FAIL}{err_msg.invalid_option}')
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
                today_order()
                if(ask_for_dashboard("Back")):
                    continue
                else:
                    break
            elif(choice == 5):
                break
            else:
                print(f'{bcolors.FAIL}{err_msg.invalid_option}')
                if(ask_for_dashboard()):
                    continue
                else:
                    break

    elif(user_state['role'] == 'admin'):
        while True:
            print(f'{bcolors.HEADER}*****************Order Page ***********************')
            print(f'{bcolors.OKBLUE}1 CANCEL ORDER')
            print('2 VIEW ORDER DETAILS')
            print('3 VIEW ALL ORDER')
            print('4 BACK')


            choice = get_input(validate_int, err_msg.choose_option, err_msg.invalid_option)
            if(not choice):
                print(f'{bcolors.FAIL}{err_msg.invalid_option}')
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
                print(f'{bcolors.FAIL}{err_msg.invalid_option}')
                if(ask_for_dashboard()):
                    continue
                else:
                    break

