

from src.utility.validation import validate_int
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.dashboard.UI.reservation_ui.reserve_table import table_reserve
from src.dashboard.UI.reservation_ui.cancel_reservation import cancel
from src.controllers.reservation_controller.reservation import get_reservation, get_all_reservaiton
from src.utility.error_message import ErrorMessage

def reservation_page():
    err_msg = ErrorMessage()
    while True:
        print('*****************Reservation Dashboard ***********************')
        print('1 BOOK TABLE')
        print('2 CANCEL BOOKING')
        print('3 VIEW BOOKING DETAILS')
        print('4 VIEW ALL BOOKING')
        print('5 BACK')

        choice = validate_int(input("please choose a option : "))

        if(not choice):
            print(err_msg.invalid_option)
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
            break
        else:
            print('please choose a valid option ')
            if(ask_for_dashboard()):
                continue
            else:
                break
