import traceback
from src.database.collections.user import User
from src.controllers.user_controller.user_state import UserState
from src.utility.validation import validate_email
from src.utility.error_message import ErrorMessage
from src.utility.log_error import LogError, log
from src.utility.get_input import get_input


def make_admin():
    try:
        USER = User()
        state = UserState().get_state()
        err_msg = ErrorMessage()
        email = get_input(validate_email, err_msg.enter_email, err_msg.invalid_email)
        if(not email):
            raise Exception(err_msg.invalid_email)

        if(state['role'] == 'super_admin'):
            for user in USER.users:
                if(user['email'] == email):
                    user['role'] = 'admin'
                    USER.save_user()
                    print(f'{user['name']} {err_msg.role_changed}')
        else:
            raise Exception(err_msg.not_authorized)
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)
        
def make_staff():
    try:
        USER = User()
        state = UserState().get_state()
        err_msg = ErrorMessage()
        email = get_input(validate_email, err_msg.enter_email, err_msg.invalid_email)
        if(not email):
            raise Exception(err_msg.invalid_email)
        
        if(state['role'] == 'super_admin'):
            for user in USER.users:
                if(user['email'] == email):
                    user['role'] = 'staff'
                    USER.save_user()
                    print(f'{user['name']} {err_msg.role_changed}')
        else:
            raise Exception(err_msg.not_authorized)
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

def get_all_user():
    try:
        err_msg = ErrorMessage()
        USER = User()
        user_state = UserState().get_state()
        fmt_str = '{:<15}{:<20}{:<20}{:<10}'
        if(USER.users):
            if(user_state['role'] == 'super_admin'):
                print(fmt_str.format('ID', 'NAME', 'EMAIL', 'ROLE'))
                print('-'*65)
                for user in USER.users:
                    print(fmt_str.format(user['id'], user['name'], user['email'], user['role']))
        else:
            print(err_msg.user_not_found)

        if(user_state['role'] == 'admin'):
                print(fmt_str.format('ID', 'NAME', 'EMAIL', 'ROLE'))
                print('-'*65)
                user_found = False
                for user in USER.users:
                    if(user['role'] == 'staff'):
                        user_found = True
                        print(fmt_str.format(user['id'], user['name'], user['email'], user['role']))
                else:
                    if(not user_found):
                        print(err_msg.user_not_found)
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

def remove_user():
    try:
        user_state = UserState().get_state()
        USER = User()
        err_msg = ErrorMessage()
        email = get_input(validate_email, err_msg.enter_email, err_msg.invalid_email)
        if(not email):
                raise Exception(err_msg.invalid_email)
        
        if(user_state['role'] == 'admin'):
            for user in USER.users:
                if(user['email'] == email):
                    if(user['role'] == 'staff'):
                        user['status'] = 'deactive'
                        USER.save_user()
                        print(f'{user['name']} {err_msg.user_remove}')
                        return
                    elif(user['role'] == 'admin' or user['role'] == 'super_admin'):
                        raise Exception(err_msg.not_authorized)
            else:
                print(err_msg.user_not_found)
        elif(user_state['role'] == 'super_admin'):
            for user in USER.users:
                if(user['email'] == email):
                    user['status'] = 'deactive'
                    USER.save_user()
                    print(f'{user['name']} {err_msg.user_remove}')
                    
        else:
            raise Exception(err_msg.not_authorized)
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

def get_current_user():
    try:
        err_msg = ErrorMessage()
        user_state = UserState().get_state()
        users = User().users

        for user in users:
            if(user['email'] == user_state['email']):
                print('\n***********PROFILE**************')
                fmt_str = '{:<20}{:<10}{:<20}'
                for name, value in user.items():
                    if(name == 'password'):
                        continue
                    if(name == 'benefits'):
                        benefits = ", ".join(value)
                        print(fmt_str.format('Benefits', ':', benefits))
                        continue
                    print(fmt_str.format(name.capitalize().replace('_', ' '), ':', value))
                return None   
        else:
            print(err_msg.user_not_found)
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

def get_user():
    try:
        user_state = UserState().get_state()
        users = User().users

        err_msg = ErrorMessage()
        email = get_input(validate_email, err_msg.enter_email, err_msg.invalid_email)
        if(not email):
            raise Exception(err_msg.invalid_email)
        fmt_str = '{:<20}{:<10}{:<20}'
        if(user_state['role'] == 'admin'):
            for user in users:
                if(user['email'] == email and user['role'] == 'staff'):
                    print('\n***********PROFILE**************')
                    for name, value in user.items():
                        if(name == 'password'):
                            continue
                        if(name == 'benefits'):
                            benefits = ", ".join(value)
                            print(fmt_str.format('Benefits', ':', benefits))
                            continue
                        print(fmt_str.format(name.capitalize().replace('_', ' '), ':', value))
                    return None
            else:
                print(err_msg.user_not_found)
        elif(user_state['role'] == 'super_admin'):
            for user in users:
                if(user['email'] == email):
                    print('\n***********PROFILE**************')
                    for name, value in user.items():
                        if(name == 'password'):
                            continue
                        if(name == 'benefits'):
                            benefits = ", ".join(value)
                            print(fmt_str.format('Benefits', ':', benefits))
                            continue
                        print(fmt_str.format(name.capitalize().replace('_', ' '), ':', value))
                    return None
            else:
                print(err_msg.user_not_found)
        else:
            raise Exception(err_msg.not_authorized)
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

#this function is no longer in use
def update_user(
        name,
        date_of_birth,
        mobile_number,
        address,
        gender
):
    USER = User()
    user_state = UserState().get_state()

    for user in USER.users:
        if(user['email'] == user_state['email']):
            user['name'] = name
            user['date_of_birth'] = date_of_birth
            user['mobile_number'] = mobile_number
            user['address'] = address
            user['gender'] = gender
            USER.save_user()
            print('profile updated')
            return
        
