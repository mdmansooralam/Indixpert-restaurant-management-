
from src.dashboard.UI.item_ui.menu import menu
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.utility.validation import validate_int
from src.dashboard.UI.order_ui.order import pay_bill, invoice
from src.controllers.user_controller.user import get_current_user
from src.dashboard.UI.pages.profile_update_page import profile_update_page
from src.dashboard.UI.pages.order_page import order_page
from src.dashboard.UI.pages.reservation_page import reservation_page
from src.utility.error_message import ErrorMessage
from src.utility.log_error import LogError
from src.utility.get_input import get_input

def staff_dashboard():
    try:
        err_msg = ErrorMessage()
        while True:
            print('*****************Welcome to staff Dashboard ***********************')
            print('1 MENU')
            print('2 ORDER')
            print('3 BILLING')
            print('4 VIEW INVOICE')
            print('5 RESERVATION')
            print('6 MY PROFILE')
            print('7 UPDATE PROFILE')
            print('8 LOGOUT')

            choice = get_input(validate_int, err_msg.choose_option, err_msg.invalid_option)
            if(not choice):
                raise Exception(err_msg.invalid_option)
            if(choice == 1):
                menu()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 2):
                order_page()
            elif(choice == 3):
                pay_bill()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 4):
                invoice()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 5):
                reservation_page()
            elif(choice == 6):
                get_current_user()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 7):
                profile_update_page()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 8):
                break
            else:
                print('please choose a valid option ')
                if(ask_for_dashboard()):
                    continue
                else:
                    break
    except Exception as error:
        print(error)
        LogError().err.exception(error)



