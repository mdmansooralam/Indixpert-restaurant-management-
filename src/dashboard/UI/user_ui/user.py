

from src.controllers.user_controller.user import update_user
from src.utility.validation import validate_name, validate_dob,validate_address,  validate_mobile, validate_gender
from src.utility.get_input import get_input
from src.utility.error_message import ErrorMessage
from src.utility.log_error import LogError

    
def update_user_profile():
    try:
        err_msg = ErrorMessage()
        name = get_input(validate_name, err_msg.enter_name, err_msg.invalid_name)
        if(not name):
            raise Exception(err_msg.invalid_name)
        gender = get_input(validate_gender, err_msg.enter_gender, err_msg.invalid_gender)
        if(gender):
            raise Exception(err_msg.invalid_gender)
    
        date_of_birth = get_input(validate_dob, err_msg.enter_dob, err_msg.invalid_dob)
        if(not date_of_birth):
            raise Exception(err_msg.invalid_dob)

        mobile_number = get_input(validate_mobile, err_msg.enter_mobile_number, err_msg.invalid_mobile_number)
        if(not mobile_number):
            raise Exception(err_msg.invalid_mobile_number)
            
        address = get_input(validate_address, err_msg.enter_address, err_msg.invalid_address)
        if(address):
            raise Exception(err_msg.invalid_address)

        update_user(name, date_of_birth, mobile_number, address, gender)

    except Exception as error:
          print(error)
          LogError().err.exception(error)