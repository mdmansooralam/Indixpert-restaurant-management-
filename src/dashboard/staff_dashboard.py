
from src.dashboard.UI.item_ui.menu import menu
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.utility.validation import validate_int
from src.dashboard.UI.order_ui.order import pay_bill, invoice
from src.controllers.user_controller.user import get_current_user
from src.dashboard.UI.user_ui.user import update_user_profile
from src.dashboard.UI.pages.order_page import order_page
from src.dashboard.UI.pages.reservation_page import reservation_page

def staff_dashboard():

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

        choice = validate_int(input("please choose a option : "))
        
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
            update_user_profile()
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


