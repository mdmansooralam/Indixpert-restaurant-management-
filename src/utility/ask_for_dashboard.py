

from src.utility.validation import validate_int
from src.utility.error_message import ErrorMessage
from src.utility.colors import bcolors
from src.utility.get_input import get_input

def ask_for_dashboard(opt='Logout'):
    err_msg = ErrorMessage()
    while True:
        choice = get_input(validate_int, f'1 Dashboard | 2 {opt} :', err_msg.invalid_option)
        if(not choice):
            return False
        else:
            if(choice == 1):
                return True
            elif(choice == 2):
                return False
            else:
                print(f'{bcolors.FAIL}{err_msg.invalid_option}')