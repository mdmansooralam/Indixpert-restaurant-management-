



from src.database.collections.error import Errors
from src.utility.get_input import get_input
from src.utility.error_message import ErrorMessage
from src.utility.validation import validate_email
from src.utility.log_error import log
from src.utility.colors import bcolors


def get_all_error():
    errors = Errors().errors
    if(errors):
        for err in errors:
            print(f'{bcolors.FAIL}DATE TIME : {err['date_time']}')
            print(f'EMAIL     : {err['email']}')
            print(f'LINE      : {err['line']}')
            print(f'SOURCE    : {err['fn_name']}')
            print(f'ERROR     : {err['err']}')
            print(f'MESSAGE   : {err['msg']}')
            print(f'PATH      : {err['path']}')
            print(f'{bcolors.OKCYAN}{'='*100}')

def get_error_by_mail():
    try:
        errors = Errors().errors
        err_msg = ErrorMessage()
        email = get_input(validate_email, err_msg.enter_email, err_msg.invalid_email)
        if(not email):
            raise Exception(err_msg.invalid_email)
        if(errors):
            print(f'==================={email}====================')
            for err in errors:
                if(err['email'] == email):
                    print(f'{bcolors.FAIL}DATE TIME : {err['date_time']}')
                    print(f'LINE      : {err['line']}')
                    print(f'SOURCE    : {err['fn_name']}')
                    print(f'ERROR     : {err['err']}')
                    print(f'MESSAGE   : {err['msg']}')
                    print(f'PATH      : {err['path']}')
                    print(f'{bcolors.OKCYAN}{'='*100}')
        else:
            print('No errors')
    except Exception as error:
        print(error)
        
