


from src.dashboard.UI.item_ui.item import create, update, delete, stock
from src.dashboard.UI.user_ui.user import  view_all_user, remove
from src.utility.validation import validate_int
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.controllers.user_controller.user import get_current_user
from src.controllers.item_controller.item import get_all_items
from src.dashboard.UI.user_ui.user import display_staff_profile, update_user_profile
from src.controllers.order_controller.order import get_all_order
from src.dashboard.UI.order_ui.order import display_order_by_date, display_order_by_days, cancel, view_order_details

def admin_dashboard():
    

    while True:
        print('\n***************welcome to RMS*****************')
        print('1 CREATE ITEM')
        print('2 DELETE ITEM')
        print('3 UPDATE ITEM')
        print('4 VIEW ITEMS')
        print('5 ADD STOCK')
        print('6 CANCEL ORDER')
        print('7 VIEW ALL STAFF')
        print('8 REMOVE STAFF')
        print('9 MY PROFILE')
        print('10 VIEW STAFF PROFILE')
        print('11 VIEW ALL ORDERS')
        print('12 VIEW ORDER DETAILS')
        print('13 VIEW ORDER BY DATE')
        print('14 VIEW ORDER BY DAYS')
        print('15 UPDATE PROFILE')
        print('16 LOGOUT')
        choice = validate_int(input('Please Choose a option : '))
        if(not choice):
            print('please choose a integer value')
        else:
            if(choice == 1):
                create()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 2):
                delete()
                if(ask_for_dashboard()):
                    continue
                else:
                    break               
            elif(choice == 3):
                update()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 4):
                get_all_items()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 5):
                stock()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 6):
                cancel()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 7):
                view_all_user()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 8):
                remove()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 9):
                get_current_user()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 10):
                display_staff_profile()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 11):
                get_all_order()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 12):
                view_order_details()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 13):
                display_order_by_date()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 14):
                display_order_by_days()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 15):
                update_user_profile()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 16):
                break
            else:
                print('please choose a valid option')

