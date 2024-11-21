





from src.controllers.reservation_controller.reservation import reserved_table
from src.utility.validation import validate_name, validate_int, validate_mobile
from src.utility.time_slot import validate_time_slot_id
from src.dashboard.UI.reservation_ui.display_time_slot import display_time_slot
from src.utility.get_input import get_input
from src.utility.error_message import ErrorMessage
from src.utility.log_error import log
import traceback

def table_reserve():
    try:
        err_msg= ErrorMessage()
        name = get_input(validate_name, err_msg.enter_name, err_msg.invalid_name)
        if(not name):
            raise Exception(err_msg.invalid_name)
        
        mobile_no = get_input(validate_mobile, err_msg.enter_mobile_number, err_msg.invalid_mobile_number)
        if(not mobile_no):
            raise Exception(err_msg.invalid_mobile_number)
        
        # date = validate_date(input('Date ( DD-MM-YYYY ) : '))
        # if(not date):
        #     raise Exception('please enter a valid date (DD-MM-YYYY)')
        
        display_time_slot()

        time_slot = get_input(validate_time_slot_id, err_msg.choose_option, err_msg.invalid_option)
        if(not time_slot):
            raise Exception(err_msg.invalid_option)
        
        persons = get_input(validate_int, err_msg.number_of_person, err_msg.invalid_number_of_person)
        if(not persons):
            print(err_msg.invalid_number_of_person)


        reserved_table(name, mobile_no, time_slot, persons)
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)