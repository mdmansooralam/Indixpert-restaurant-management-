


from src.utility.validation import validate_int
from src.utility.ask_for_dashboard import ask_for_dashboard
from src.controllers.item_controller.item import view_stock
from src.dashboard.UI.item_ui.item import stock
from src.utility.error_message import ErrorMessage
from src.utility.get_input import get_input


def stock_page():
    err_msg = ErrorMessage()
    while True:
        print('*****************Stock Page ***********************')
        print('1 VIEW STOCK')
        print('2 ADD STOCK')
        print('3 BACK')

        choice = get_input(validate_int, err_msg.choose_option, err_msg.invalid_option)

        if(not choice):
            print(err_msg.invalid_option)
        elif(choice == 1):
            view_stock()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 2):
            stock()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 3):
            break
        else:
            print(err_msg.invalid_option)
            if(ask_for_dashboard()):
                continue
            else:
                break

