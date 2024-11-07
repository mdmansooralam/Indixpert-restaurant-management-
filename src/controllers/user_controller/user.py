
from src.database.collections.user import User
from src.controllers.user_controller.user_state import UserState
from src.utility.validation import validate_email
from src.utility.error_message import ErrorMessage


def make_admin():
    try:
        USER = User()
        state = UserState().get_state()
        err_msg = ErrorMessage()
        email = validate_email(input("Enter Email : "))
        if(not email):
            raise Exception(err_msg.invalid_email)

        if(state['role'] == 'super_admin'):
            for user in USER.users:
                if(user['email'] == email):
                    user['role'] = 'admin'
                    USER.save_user()
                    print(f'{user['name']} role has been changed to admin')
        else:
            raise Exception(err_msg.not_authorized)
    except Exception as error:
        print(error)

def make_staff():
    try:
        USER = User()
        state = UserState().get_state()
        err_msg = ErrorMessage()
        email = validate_email(input("Enter Email : "))
        if(not email):
            raise Exception(err_msg.invalid_email)
        
        if(state['role'] == 'super_admin'):
            for user in USER.users:
                if(user['email'] == email):
                    user['role'] = 'staff'
                    USER.save_user()
                    print(f'{user['name']} role has been changed to staff')
        else:
            raise Exception(err_msg.not_authorized)
    except Exception as error:
        print(error)

def get_all_user():
        USER = User()
        user_state = UserState().get_state()
        if(USER.users):
            if(user_state['role'] == 'super_admin'):
                print('{:<15}{:<20}{:<20}{:<10}'.format('ID', 'NAME', 'EMAIL', 'ROLE'))
                print('-'*65)
                for user in USER.users:
                    print('{:<15}{:<20}{:<20}{:<10}'.format(user['id'], user['name'], user['email'], user['role']))
        else:
            print('user record not found')

        if(user_state['role'] == 'admin'):
                print('{:<15}{:<20}{:<20}{:<10}'.format('ID', 'NAME', 'EMAIL', 'ROLE'))
                print('-'*55)
                user_found = False
                for user in USER.users:
                    if(user['role'] == 'staff'):
                        user_found = True
                        print('{:<15}{:<20}{:<20}{:<10}'.format(user['id'], user['name'], user['email'], user['role']))
                else:
                    if(not user_found):
                        print('user not found')

def remove_user():
    try:
        user_state = UserState().get_state()
        USER = User()
        err_msg = ErrorMessage()
        email = validate_email(input("Enter Email : "))
        if(not email):
                raise Exception(err_msg.invalid_email)
        if(user_state['role'] == 'admin'):
            for user in USER.users:
                if(user['email'] == email):
                    if(user['role'] == 'staff'):
                        user['status'] = 'deactive'
                        USER.save_user()
                        print(f'{user['name']} removed successful')
                        break
                    elif(user['role'] == 'admin' or user['role'] == 'super_admin'):
                        raise Exception(err_msg.not_authorized)
            else:
                print('user not found')
        elif(user_state['role'] == 'super_admin'):
            for user in USER.users:
                if(user['email'] == email):
                    user['status'] = 'deactive'
                    USER.save_user()
                    print(f'{user['name']} removed successful')
                    
        else:
            raise Exception(err_msg.not_authorized)
    except Exception as error:
        print(error)

def get_current_user():
    user_state = UserState().get_state()
    users = User().users

    for user in users:
        if(user['email'] == user_state['email']):
            print('\n***********PROFILE**************')
            for name, value in user.items():
                if(name == 'password'):
                    continue
                if(name == 'benefits'):
                    benefits = ", ".join(value)
                    print('{:<20}{:<10}{:<20}'.format('Benefits', ':', benefits))
                    continue
                print('{:<20}{:<10}{:<20}'.format(name.capitalize().replace('_', ' '), ':', value))
            return None   
    else:
        print('current user not available')

def get_user():
    try:
        user_state = UserState().get_state()
        users = User().users

        err_msg = ErrorMessage()
        email = validate_email(input("Enter Email : "))
        if(not email):
            raise Exception(err_msg.invalid_email)
        
        if(user_state['role'] == 'admin'):
            for user in users:
                if(user['email'] == email and user['role'] == 'staff'):
                    print('\n***********PROFILE**************')
                    for name, value in user.items():
                        if(name == 'password'):
                            continue
                        if(name == 'benefits'):
                            benefits = ", ".join(value)
                            print('{:<20}{:<10}{:<20}'.format('Benefits', ':', benefits))
                            continue
                        print('{:<20}{:<10}{:<20}'.format(name.capitalize().replace('_', ' '), ':', value))
                    return None
            else:
                print('user not found')
        elif(user_state['role'] == 'super_admin'):
            for user in users:
                if(user['email'] == email):
                    print('\n***********PROFILE**************')
                    for name, value in user.items():
                        if(name == 'password'):
                            continue
                        if(name == 'benefits'):
                            benefits = ", ".join(value)
                            print('{:<20}{:<10}{:<20}'.format('Benefits', ':', benefits))
                            continue
                        print('{:<20}{:<10}{:<20}'.format(name.capitalize().replace('_', ' '), ':', value))
                    return None
            else:
                print('user not found')
        else:
            raise Exception(err_msg.not_authorized)
    except Exception as error:
        print(error)

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
        
