

from src.controllers.user_controller.update_profile import update_address, update_dob, update_gender, update_mobile, update_name, update_password
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.utility.get_input import get_input
from src.utility.validation import validate_int
from src.utility.colors import bcolors
from src.utility.error_message import ErrorMessage

def profile_update_page():
    err_msg = ErrorMessage()
    while True:
        print(f'{bcolors.HEADER}*****************Profile Update Page ***********************')
        print(f'{bcolors.OKBLUE}1 UPDATE NAME')
        print('2 UPDATE DATE OF BIRTH')
        print('3 UPDATE ADDRESS')
        print('4 UPDATE MOBILE NUMBER')
        print('5 UPDATE GENDER')
        print('6 UPDATE PASSWORD')
        print('7 BACK')

        choice = get_input(validate_int, err_msg.choose_option, err_msg.invalid_option)

        if(not choice):
            print(f'{bcolors.FAIL}{err_msg.invalid_option}')

        elif(choice == 1):
            update_name()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 2):
            update_dob()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 3):
            update_address()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 4):
            update_mobile()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 5):
            update_gender()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 6):
            update_password()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 7):
            break
        else:
            print(f'{bcolors.FAIL}{err_msg.invalid_option}')
            if(ask_for_dashboard()):
                continue
            else:
                break

