
from src.database.collections.user import User
from src.controllers.user_controller.user_state import UserState


def make_admin(email):
        USER = User()
        state = UserState().get_state()
        if(state['role'] == 'super_admin'):
            for user in USER.users:
                if(user['email'] == email):
                    user['role'] = 'admin'
                    USER.save_user()
                    print(f'{user['name']} role has been changed to admin')
        else:
            print('your are not authorized for this operation')

def make_staff(email):
        USER = User()
        state = UserState().get_state()
        if(state['role'] == 'super_admin'):
            for user in USER.users:
                if(user['email'] == email):
                    user['role'] = 'staff'
                    USER.save_user()
                    print(f'{user['name']} role has been changed to staff')
        else:
            print('your are not authorized for this operation')

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

def remove_user(email):
    user_state = UserState().get_state()
    USER = User()
    if(user_state['role'] == 'admin'):
        for user in USER.users:
            if(user['email'] == email):
                if(user['role'] == 'staff'):
                    user['status'] = 'deactive'
                    USER.save_user()
                    print(f'{user['name']} removed successful')
                    break
                elif(user['role'] == 'admin' or user['role'] == 'super_admin'):
                     print('Your are not authorized to remove ADMIN or SUPER_ADMIN')
        else:
             print('user not found')
    elif(user_state['role'] == 'super_admin'):
        for user in USER.users:
            if(user['email'] == email):
                user['status'] = 'deactive'
                USER.save_user()
                print(f'{user['name']} removed successful')
                  
    else:
        print('you are not authorized')

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

def get_user_by_email(email):
    user_state = UserState().get_state()
    users = User().users

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
        print('you are not authorized ')

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
        
