from src.utility.log_error import LogError
from src.utility.colors import bcolors

def get_input(validator, msg, err_msg):
    while True:
        try:
            user_input = input(f'{bcolors.OKCYAN}{msg}')
            if(user_input.lower() == 'exit'):
                return False
            result = validator(user_input)
            if(result):
                return result
            else:
                # print(err_msg)
                raise Exception(err_msg)
        except Exception as error:
            print(f'{bcolors.FAIL}{error}')