



from src.utility.ask_for_dashboard import ask_for_dashboard
from src.utility.validation import validate_int
from src.utility.error_message import ErrorMessage
from src.controllers.order_controller.order_report import get_order_staff_wise, get_all_order, get_order_by_date, get_order_by_day






def report_page():
    err_msg = ErrorMessage()
    while True:
        print('*****************Report Page ***********************')
        print('1 VIEW ALL ORDERS')
        print('2 VIEW ORDER BY DATE')
        print('3 VIEW ORDER BY DAYS')
        print('4 STAFF WISE')
        print('5 BACK')

        choice = validate_int(input("please choose a option : "))

        if(not choice):
            print(err_msg.invalid_option)
        elif(choice == 1):
            get_all_order()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 2):
            get_order_by_date()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 3):
            get_order_by_day()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 4):
            get_order_staff_wise()
            if(ask_for_dashboard("Back")):
                continue
            else:
                break
        elif(choice == 5):
            break
        else:
            print(err_msg.invalid_option)
            if(ask_for_dashboard()):
                continue
            else:
                break