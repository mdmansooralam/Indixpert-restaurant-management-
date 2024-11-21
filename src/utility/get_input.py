from src.utility.colors import bcolors
import maskpass

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

def get_password(validator, msg, err_msg):
    while True:
        try:
            user_input = maskpass.askpass(f'{bcolors.OKCYAN}{msg}')
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