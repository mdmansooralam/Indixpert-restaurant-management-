





from src.controllers.order_controller.order_report import get_order_by_date, get_order_by_day
from src.utility.validation import validate_id
from src.controllers.order_controller.order import payment_proceed
from src.controllers.order_controller.order_report import view_invoice, get_order_details
from src.utility.get_input import get_input
from src.utility.error_message import ErrorMessage
from src.utility.log_error import LogError, log
import traceback

def display_order_by_date():
    get_order_by_date()

def display_order_by_days():
    get_order_by_day()

def pay_bill():
    try:
        err_msg = ErrorMessage()
        id = get_input(validate_id, err_msg.enter_id, err_msg.invalid_id)
        if(not id):
            raise Exception(err_msg.invalid_id)
        payment_proceed(id)
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

def invoice():
    try:
        err_msg = ErrorMessage()
        order_id = get_input(validate_id, err_msg.enter_id, err_msg.invalid_id)
        if(not order_id):
            raise Exception(err_msg.invalid_id)
        view_invoice(order_id)
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

def view_order_details():
    try:
        err_msg = ErrorMessage()
        order_id = get_input(validate_id, err_msg.enter_id, err_msg.invalid_id)
        if(not order_id):
            raise Exception(err_msg.invalid_id)
        get_order_details(order_id)
    
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

