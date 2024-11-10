


from src.dashboard.UI.auth_ui.auth import login, signup
from src.utility.validation import validate_int
from src.utility.error_message import ErrorMessage
from src.utility.get_input import get_input
from src.utility.log_error import LogError

def authentication():
    err_msg = ErrorMessage()
    while True:
        print('**********USER AUTHENTICATION***********')
        print('1 LOGIN')
        print('2 SIGNUP')
        print('3 EXIT')


        choice = get_input(validate_int, err_msg.choose_option, err_msg.invalid_option)
        if(not choice):
            LogError().err.exception(err_msg.invalid_option)
            break
        
        if(choice == 1):
            login()
        elif(choice == 2):
            signup()
        elif(choice == 3):
            break
        else:
            print(err_msg.invalid_option)
