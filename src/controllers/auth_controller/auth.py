import uuid

from src.database.collections.user import User
from src.models.user_model import UserModel
from src.utility.check_user import check_user
from src.controllers.user_controller.super_admin import super_admin
from src.controllers.user_controller.user_state import UserState
from src.dashboard.manage_dashboard import dashboard




def user_signup(name, email, password):
        try:
            USER = User()
            user = check_user(email)
            if(user):
                print('user already register with this email....')     
            else:
                id = str(uuid.uuid4())[:10]
                role = 'staff'
                new_user = UserModel(id, name, email, password, role).__dict__
                USER.users.append(new_user)
                USER.save_user()
                print('signup successful please login ....')
        except Exception as error:
             print(error)


def user_login(email, password):
        try:
            USER = User()
            if(email == 'super@admin.com' and password == 'Super@123'):
                super_admin(email, password)
            else:
                user = check_user(email)
                if(not user):
                    print('user not exist')
                else:
                    for user in USER.users:
                        if(user['email'] == email):
                            if(user['password'] == password):
                                UserState().update_state(user)
                                dashboard()

                            else:
                                print('wrong credential pleae try again.....')
        except Exception as error:
             print(error)