




from src.utility.validation import validate_int
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.controllers.user_controller.user import get_all_user, remove_user, get_user
from src.utility.error_message import ErrorMessage
from src.utility.get_input import get_input
from src.utility.colors import bcolors


def staff_page():
    err_msg = ErrorMessage()
    while True:
        print(f'{bcolors.HEADER}*****************Staff Page ***********************')
        print(f'{bcolors.OKBLUE}1 VIEW ALL STAFF')
        print('2 VIEW STAFF PROFILE')
        print('3 REMOVE STAFF')
        print('4 BACK')

        choice = get_input(validate_int, err_msg.choose_option, err_msg.invalid_option)

        if(not choice):
            print(f'{bcolors.FAIL}{err_msg.invalid_option}')
        elif(choice == 1):
            get_all_user()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 2):
            get_user()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 3):
            remove_user()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 4):
            break
        else:
            print(f'{bcolors.FAIL}{err_msg.invalid_option}')
            if(ask_for_dashboard()):
                continue
            else:
                break

