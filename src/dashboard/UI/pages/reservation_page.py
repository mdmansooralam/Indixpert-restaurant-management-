

from src.utility.validation import validate_int
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.dashboard.UI.reservation_ui.reserve_table import table_reserve
from src.dashboard.UI.reservation_ui.cancel_reservation import cancel
from src.controllers.reservation_controller.reservation import get_reservation, get_all_reservaiton, get_available_table
from src.utility.error_message import ErrorMessage
from src.utility.get_input import get_input
from src.utility.colors import bcolors

def reservation_page():
    err_msg = ErrorMessage()
    while True:
        print(f'{bcolors.HEADER}*****************Reservation Page ***********************')
        print(f'{bcolors.OKBLUE}1 BOOK TABLE')
        print('2 CANCEL BOOKING')
        print('3 SEARCH BOOKING')
        print('4 VIEW ALL BOOKING')
        print('5 VIEW AVAILABLE TABLE')
        print('6 BACK')

        choice = get_input(validate_int, err_msg.choose_option, err_msg.invalid_option)

        if(not choice):
            print(f'{bcolors.FAIL}{err_msg.invalid_option}')
        elif(choice == 1):
            table_reserve()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 2):
            cancel()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 3):
            get_reservation()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 4):
            get_all_reservaiton()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 5):
            get_available_table()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 6):
            break
        else:
            print(f'{bcolors.FAIL}{err_msg.invalid_option}')
            if(ask_for_dashboard()):
                continue
            else:
                break

