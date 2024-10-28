

from src.dashboard.UI.item_ui.menu import menu
from src.dashboard.UI.order_ui.order_system  import order_system
from src.controllers.order_controller.update_order import update_order
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.utility.validation import validate_int
from src.dashboard.UI.reservation_ui.reserve_table import table_reserve
from src.dashboard.UI.reservation_ui.cancel_reservation import cancel
from src.controllers.user_controller.user import get_current_user

def staff_dashboard():

    while True:
        print('*****************Welcome to staff Dashboard ***********************')
        print('1 Menu')
        print('2 Create Order')
        print('3 update order')
        print('4 Reserve Table')
        print('5 Cancel Reservation')
        print('6 View Reservation')
        print('7 View All Rerservation')
        print('8 My Profile')
        print('9 Logout')

        choice = validate_int(input("please choose a option : "))
        
        if(choice == 1):
            menu()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 2):
            order_system()

            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 3):
            update_order()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 4):
            table_reserve()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 5):
            cancel()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 6):
            pass
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 7):
            pass
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 8):
            get_current_user()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 9):
            break
        else:
            print('please choose a valid option ')
            if(ask_for_dashboard()):
                continue
            else:
                break


