
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.utility.validation import validate_int
from src.controllers.user_controller.user import make_admin, make_staff, get_all_user, remove_user

def super_admin_dashboard():


    while True:
        print('\n*****************welcome to super admin dashboard*******************')
        print('1 MAKE ADMIN')
        print('2 MAKE STAFF')
        print('3 VIEW ALL USERS')
        print('4 REMOVE USER')
        print('5 LOGOUT')

        
        choice = validate_int(input('choose a option : '))
        if(not choice):
            print('please enter a valid integer option')
        else:
            if(choice == 1):
                make_admin()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            if(choice == 2):
                make_staff()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 3):
                get_all_user()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 4):
                remove_user()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 5):
                break
            else:
                print('please choose a valid option')

