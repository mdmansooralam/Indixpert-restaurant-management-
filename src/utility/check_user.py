

from src.user_management.user import User


def check_user(email):
    users = User().users
    
    for user in  users:
        if(user.email == email):
            return True

