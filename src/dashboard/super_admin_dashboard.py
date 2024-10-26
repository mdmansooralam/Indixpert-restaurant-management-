
from src.dashboard.UI.user_ui.user import admin, remove, view_all_user
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.utility.validation import validate_int

def super_admin_dashboard():

    print('\n*****************welcome to super admin dashboard*******************')
    print('1 Make Admin')
    print('2 View all users')
    print('3 REMOVE USER')
    print('4 Logout')

    while True:
        choice = validate_int(input('choose a option : '))
        if(not choice):
            print('please enter a valid integer option')
        else:
            if(choice == 1):
                admin()
                if(ask_for_dashboard()):
                    continue
                else:
                    break

            elif(choice == 2):
                view_all_user()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 3):
                remove()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
                
            elif(choice == 4):
                break
            else:
                print('please choose a valid option')

        