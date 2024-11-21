import traceback
from src.utility.validation import validate_name, validate_gender, validate_mobile, validate_dob, validate_password, validate_address
from src.utility.error_message import ErrorMessage
from src.utility.log_error import LogError, log
from src.database.collections.user import User
from src.utility.get_input import get_input, get_password
from src.controllers.user_controller.user_state import UserState


def update_name():
    try:
        err_msg = ErrorMessage()
        user_state = UserState().get_state()
        USER = User()

        name = get_input(validate_name, err_msg.enter_name, err_msg.invalid_name)
        if(not name):
            raise Exception(err_msg.invalid_name)
        
        for user in USER.users:
            if(user_state['email'] == user['email']):
                user['name'] = name
                USER.save_user()
                print(err_msg.profile_updated)
                return
        raise Exception(err_msg.err_in_profile_upate)
    
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

def update_mobile():
    try:
        err_msg = ErrorMessage()
        user_state = UserState().get_state()
        USER = User()

        mobile_number = get_input(validate_mobile, err_msg.enter_mobile_number, err_msg.invalid_mobile_number)
        if(not mobile_number):
            raise Exception(err_msg.invalid_mobile_number)
        
        for user in USER.users:
            if(user_state['email'] == user['email']):
                user['mobile_number'] = mobile_number
                USER.save_user()
                print(err_msg.profile_updated)
                return
        raise Exception(err_msg.err_in_profile_upate)
    
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

def update_dob():
    try:
        err_msg = ErrorMessage()
        user_state = UserState().get_state()
        USER = User()

        date_of_birth = get_input(validate_dob, err_msg.enter_dob, err_msg.invalid_dob)
        if(not date_of_birth):
            raise Exception(err_msg.invalid_dob)
        
        for user in USER.users:
            if(user_state['email'] == user['email']):
                user['date_of_birth'] = date_of_birth
                USER.save_user()
                print(err_msg.profile_updated)
                return
        raise Exception(err_msg.err_in_profile_upate)
    
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)
    
def update_password():
    try:
        err_msg = ErrorMessage()
        user_state = UserState().get_state()
        USER = User()

        password = get_password(validate_password, err_msg.enter_password, err_msg.invalid_password)
        if(not password):
            raise Exception(err_msg.invalid_password)
        
        for user in USER.users:
            if(user_state['email'] == user['email']):
                user['password'] = password
                USER.save_user()
                print(err_msg.profile_updated)
                return
        raise Exception(err_msg.err_in_profile_upate)
    
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

def update_address():
    try:
        err_msg = ErrorMessage()
        user_state = UserState().get_state()
        USER = User()

        address = get_input(validate_address, err_msg.enter_address, err_msg.invalid_address)
        if(not address):
            raise Exception(err_msg.invalid_address)
        
        for user in USER.users:
            if(user_state['email'] == user['email']):
                user['address'] = address
                USER.save_user()
                print(err_msg.profile_updated)
                return
        raise Exception(err_msg.err_in_profile_upate)
    
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

def update_gender():
    try:
        err_msg = ErrorMessage()
        user_state = UserState().get_state()
        USER = User()

        gender = get_input(validate_gender, err_msg.enter_gender, err_msg.invalid_gender)
        if(not gender):
            raise Exception(err_msg.invalid_gender)
        
        for user in USER.users:
            if(user_state['email'] == user['email']):
                user['gender'] = gender
                USER.save_user()
                print(err_msg.profile_updated)
                return
        raise Exception(err_msg.err_in_profile_upate)
    
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)


