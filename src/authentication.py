


from src.dashboard.UI.auth_ui.auth import login, signup
from src.utility.validation import validate_int
from src.utility.error_message import ErrorMessage
from src.utility.get_input import get_input
from src.utility.colors import bcolors

def authentication():
    err_msg = ErrorMessage()
    while True:
        print(f'{bcolors.HEADER}**********USER AUTHENTICATION***********')
        print(f'{bcolors.OKBLUE}1 LOGIN')
        print('2 SIGNUP')
        print('3 EXIT')


        choice = get_input(validate_int, err_msg.choose_option, err_msg.invalid_option)
        if(not choice):
            print(err_msg.invalid_option)
            break
        
        if(choice == 1):
            login()
        elif(choice == 2):
            signup()
        elif(choice == 3):
            break
        else:
            print(f'{bcolors.FAIL}{err_msg.invalid_option}')
