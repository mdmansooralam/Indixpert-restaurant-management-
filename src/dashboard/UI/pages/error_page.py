from src.controllers.error_controller.error import get_all_error, get_error_by_mail
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.utility.get_input import get_input
from src.utility.validation import validate_int
from src.utility.colors import bcolors
from src.utility.error_message import ErrorMessage

def error_page():
    err_msg = ErrorMessage()
    while True:
        print(f'{bcolors.HEADER}*****************Error Page ***********************')
        print(f'{bcolors.OKBLUE}1 VIEW ALL ERROR')
        print('2 SEARCH ERROR')
        print('3 BACK')

        choice = get_input(validate_int, err_msg.choose_option, err_msg.invalid_option)

        if(not choice):
            print(f'{bcolors.FAIL}{err_msg.invalid_option}')

        elif(choice == 1):
            get_all_error()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 2):
            get_error_by_mail()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 3):
            break
        else:
            print(f'{bcolors.FAIL}{err_msg.invalid_option}')
            if(ask_for_dashboard()):
                continue
            else:
                break

