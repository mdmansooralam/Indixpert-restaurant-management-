
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.utility.validation import validate_int
from src.controllers.user_controller.user import make_admin, make_staff, get_all_user, remove_user
from src.utility.get_input import get_input
from src.utility.error_message import ErrorMessage
from src.utility.colors import bcolors

def super_admin_dashboard():

    err_msg = ErrorMessage()
    while True:
        print(f'{bcolors.HEADER}\n*****************welcome to super admin dashboard*******************')
        print(f'{bcolors.OKBLUE}1 MAKE ADMIN')
        print('2 MAKE STAFF')
        print('3 VIEW ALL USERS')
        print('4 REMOVE USER')
        print('5 LOGOUT')

        
        choice = get_input(validate_int, err_msg.choose_option, err_msg.invalid_option)
        if(not choice):
            print(f'{bcolors.FAIL}{err_msg.invalid_option}')
            continue
        else:
            if(choice == 1):
                make_admin()
                if(ask_for_dashboard()):
                    continue
                else:
                    break
            elif(choice == 2):
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
                print(f'{bcolors.FAIL}{err_msg.invalid_option}')

