import uuid


from src.models.user_model import UserModel
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
                new_user = UserModel(id, name, email, password, role)
                self.user.users.append(new_user)
                self.user.save_user()
                print(f'signup successful, please login')
        except Exception as error:
            print(error)

    def user_login(self, email, password):
        for user in self.user.users:
            if(user.email == email):
                if(user.password == password):
                    #update state and send to dashboard management
                    pass
                else:
                    print('wrong credential please try with correct data')
                    break


