
from src.database.collections.user import User

def check_user(email):
    user = User()
    user_found = False
    for user in user.users:
        if(user['email'] == email):
            user_found = True
            return True
    else:
        if(not user_found):
            return False