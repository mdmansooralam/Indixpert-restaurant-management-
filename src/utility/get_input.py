from src.utility.log_error import LogError

def get_input(validator, msg, err_msg):
    while True:
        try:
            user_input = input(msg)
            if(user_input.lower() == 'exit'):
                return False
            result = validator(user_input)
            if(result):
                return result
            else:
                # print(err_msg)
                raise Exception(err_msg)
        except Exception as error:
            print(error)
            LogError().err.exception(user_input)