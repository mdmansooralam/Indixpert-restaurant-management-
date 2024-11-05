

from src.dashboard.UI.item_ui.menu import menu
from src.dashboard.UI.order_ui.order_system  import order_system
from src.controllers.order_controller.update_order import update_order
from src.controllers.order_controller.order import get_unpaid_order
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.utility.validation import validate_int
from src.dashboard.UI.reservation_ui.reserve_table import table_reserve
from src.dashboard.UI.reservation_ui.cancel_reservation import cancel
from src.controllers.user_controller.user import get_current_user
from src.dashboard.UI.order_ui.order import pay_bill, invoice
from src.controllers.reservation_controller.reservation import get_all_reservaiton, get_reservation
from src.dashboard.UI.user_ui.user import update_user_profile
from src.utility.restaurant_status import restaurant_status

def staff_dashboard():

    while True:
        print('*****************Welcome to staff Dashboard ***********************')
        print('1 MENU')
        print('2 CREATE ORDER')
        print('3 UPDATE ORDER')
        print('4 ORDER IN PROCESS')
        print('5 BILLING')
        print('6 VIEW INVOICE')
        print('7 RESERVE TABLE')
        print('8 CANCEL RESERVATION')
        print('9 VIEW RESERVATION')
        print('10 VIEW ALL RESERVATION')
        print('11 MY PROFILE')
        print('12 UPDATE PROFILE')
        print('13 LOGOUT')

        choice = validate_int(input("please choose a option : "))
        
        if(choice == 1):
            menu()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 2):
            if(restaurant_status()):
                order_system()

            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 3):
            if(restaurant_status()):
                update_order()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 4):
            get_unpaid_order()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 5):
            if(restaurant_status()):
                pay_bill()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 6):
            invoice()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 7):
            table_reserve()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 8):
            cancel()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 9):
            get_reservation()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 10):
            get_all_reservaiton()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 11):
            get_current_user()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 12):
            update_user_profile()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 13):
            break
        else:
            print('please choose a valid option ')
            if(ask_for_dashboard()):
                continue
            else:
                break


