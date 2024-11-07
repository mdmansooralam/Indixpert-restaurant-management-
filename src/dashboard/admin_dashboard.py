
from src.utility.validation import validate_int
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.controllers.user_controller.user import get_current_user
from src.dashboard.UI.user_ui.user import update_user_profile
from src.dashboard.UI.pages.item_page import item_page
from src.dashboard.UI.pages.stock_page import stock_page
from src.dashboard.UI.pages.order_page import order_page
from src.dashboard.UI.pages.staff_page import staff_page
from src.utility.error_message import ErrorMessage

def admin_dashboard():
    err_msg = ErrorMessage()

    while True:
        print('\n***************welcome to RMS*****************')
        print('1 ITEM')
        print('2 STOCK')
        print('3 ORDER')
        print('4 REPORTS')#all orders, orders by date, order by days
        print('5 STAFF')
        print('6 MY PROFILE')
        print('7 UPDATE PROFILE')
        print('8 LOGOUT')

        choice = validate_int(input('Please Choose a option : '))

        if(not choice):
            print(err_msg.invalid_option)

        elif(choice == 1):
            item_page()
        elif(choice == 2):
            stock_page()
        elif(choice == 3):
            order_page()
        elif(choice == 4):
            pass
        elif(choice == 5):
            staff_page()
        elif(choice == 6):
            get_current_user()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 7):
            update_user_profile()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == 8):
            break
        else:
            print('please choose a valid option')

