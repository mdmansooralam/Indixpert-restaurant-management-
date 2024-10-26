

from src.dashboard.UI.order_ui.display_menu_feature import display_menu
from src.dashboard.UI.order_ui.order_system  import order_system
from src.controllers.order_controller.update_order import update_order
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.utility.validation import validate_int
from src.dashboard.UI.reservation_ui.reserve_table import table_reserve

def staff_dashboard():

    while True:
        print('*****************Welcome to staff Dashboard ***********************')
        print('1 Menu')
        print('2 Create Order')
        print('3 update order')
        print('4 Reserve Table')
        print('5 Logout')

        choice = validate_int(input("please choose a option : "))
        
        if(choice == 1):
            display_menu()
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
            break
        else:
            print('please choose a valid option ')
            if(ask_for_dashboard()):
                continue
            else:
                break


