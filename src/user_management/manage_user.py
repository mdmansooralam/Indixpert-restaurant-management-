import uuid


from src.user_management.user import User
from src.utility.check_user import check_user


class ManageUser:
    def __init__(self):
        self.user = User()

    def user_signup(self, name, email, password):
        try:
            user = check_user(email)
            if(user):
                print('user already register...')
            else:
                id = str(uuid.uuid4())[:10]
                role = 'staff'
                new_user = User(id, name, email, password, role)
                self.user.users.append(new_user)
                self.user.save_user()
                print(f'signup successful, please login')
        except Exception as error:
            print(error)



