
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
                    USER.users.remove(user)
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
                USER.users.remove(user)
                USER.save_user()
                print(f'{user['name']} removed successful')
                  
    else:
        print('you are not authorized')

