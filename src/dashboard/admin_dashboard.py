


from src.dashboard.UI.item_ui.item import create, update, delete
from src.dashboard.UI.user_ui.user import  view_all_user, remove
from src.utility.validation import validate_int
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.controllers.user_controller.user import get_current_user
from src.dashboard.UI.user_ui.user import display_staff_profile

def admin_dashboard():
    

    while True:
        print('\n***************welcome to RMS*****************')
        print('1 CREATE ITEM')
        print('2 DELETE ITEM')
        print('3 UPDATE ITEM')
        print('4 VIEW ALL STAFF')
        print('5 REMOVE STAFF')
        print('6 MY PROFILE')
        print('7 VIEW STAFF PROFILE')
        print('8 LOGOUT')
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
                view_all_user()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 5):
                remove()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 6):
                get_current_user()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 7):
                display_staff_profile()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 8):
                break
            else:
                print('please choose a valid option')

