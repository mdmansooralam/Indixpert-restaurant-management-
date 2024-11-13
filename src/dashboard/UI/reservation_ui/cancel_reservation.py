




from src.controllers.reservation_controller.reservation import cancel_reservaiton
from src.utility.validation import validate_id
from src.utility.error_message import ErrorMessage
from src.utility.log_error import LogError
from src.utility.get_input import get_input
from src.utility.colors import bcolors


def cancel():
    try:
        err_msg = ErrorMessage()

        id = get_input(validate_id, err_msg.enter_id, err_msg.invalid_id)
        if(not id):
            raise Exception(err_msg.invalid_id)
        
        cancel_reservaiton(id)

    except Exception as error:
        print(f'{bcolors.FAIL}{error}')
        LogError().err.exception(error)