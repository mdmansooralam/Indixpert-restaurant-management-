




from src.utility.validation import validate_int
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.dashboard.UI.item_ui.item import create, update, delete
from src.utility.error_message import ErrorMessage
from src.utility.get_input import get_input
from src.utility.colors import bcolors


def item_page():
    err_msg = ErrorMessage()
    while True:
        print(f'{bcolors.HEADER}*****************Item Page ***********************')
        print(f'{bcolors.OKBLUE}1 ADD ITEM')
        print('2 UPDATE ITEM')
        print('3 DELETE ITEM')
        print('4 BACK')

        choice = get_input(validate_int, err_msg.choose_option, err_msg.invalid_option)

        if(not choice):
            print(f'{bcolors.FAIL}{err_msg.invalid_option}')
            continue
        elif(choice == 1):
            create()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 2):
            update()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 3):
            delete()
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

