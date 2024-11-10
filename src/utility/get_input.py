

def get_input(validator, msg, err_msg):
    while True:
        user_input = input(msg)
        if(user_input.lower() == 'exit'):
            return False
        result = validator(user_input)
        if(result):
            return result
        else:
            print(err_msg)