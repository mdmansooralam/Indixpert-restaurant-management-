


from src.dashboard.UI.item_ui.item import create, update, delete
from src.dashboard.UI.user_ui.user import  view_all_user, remove
from src.utility.validation import validate_int
from src.utility.ask_for_dashboard import ask_for_dashboard

def admin_dashboard():
    

    while True:
        print('\n***************welcome to RMS*****************')
        print('1 CREATE ITEM')
        print('2 DELETE ITEM')
        print('3 UPDATE ITEM')
        print('4 VIEW ALL STAFF')
        print('5 REMOVE STAFF')
        print('6 LOGOUT')
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
                break

            else:
                print('please choose a valid option')