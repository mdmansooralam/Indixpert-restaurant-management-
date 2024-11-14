

from datetime import datetime
import traceback
from src.database.collections.error import Errors
from src.utility.get_input import get_input
from src.utility.error_message import ErrorMessage
from src.utility.validation import validate_email, validate_date
from src.utility.log_error import log
from src.utility.colors import bcolors


def get_all_error():
    try:
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
        else:
            print(f'{bcolors.FAIL}No errors')
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

def get_error_by_mail():
    try:
        errors = Errors().errors
        err_msg = ErrorMessage()
        email = get_input(validate_email, err_msg.enter_email, err_msg.invalid_email)
        if(not email):
            raise Exception(err_msg.invalid_email)
        if(errors):
            print(f'==================={email}====================')
            err_found = False
            for err in errors:
                if(err['email'] == email):
                    err_found = True
                    print(f'{bcolors.FAIL}DATE TIME : {err['date_time']}')
                    print(f'LINE      : {err['line']}')
                    print(f'SOURCE    : {err['fn_name']}')
                    print(f'ERROR     : {err['err']}')
                    print(f'MESSAGE   : {err['msg']}')
                    print(f'PATH      : {err['path']}')
                    print(f'{bcolors.OKCYAN}{'='*100}')
            if(not err_found):
                print(f'{bcolors.FAIL}No errors')
        else:
            print('No errors')
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)
        
def get_error_by_date():
    try:
        err_msg = ErrorMessage()
        errors = Errors().errors
        date = get_input(validate_date, err_msg.enter_date, err_msg.invalid_date)
        if(not date):
            raise Exception(err_msg.invalid_date)
        err_found = False
        for err in errors:
            err_date = datetime.strptime(err['date_time'], '%Y-%m-%d %H:%M:%S.%f').date().strftime('%d-%m-%Y')
            if(err_date == date):
                err_found = True
                print(f'{bcolors.FAIL}DATE TIME : {err['date_time']}')
                print(f'EMAIL     : {err['email']}')
                print(f'LINE      : {err['line']}')
                print(f'SOURCE    : {err['fn_name']}')
                print(f'ERROR     : {err['err']}')
                print(f'MESSAGE   : {err['msg']}')
                print(f'PATH      : {err['path']}')
                print(f'{bcolors.OKCYAN}{'='*100}')
        if(not err_found):
            print(f'{bcolors.FAIL}No errors')

            
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)