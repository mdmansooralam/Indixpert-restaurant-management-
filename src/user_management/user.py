import os
import json
from src.models.user import UserModel

USER_FILE = 'src/database/user.json'


class User:
    def __init__(self):
        self.users = self.load_user()

    def load_user(self):
        try:
            if os.path.exists(USER_FILE):
                with open(USER_FILE, 'r') as file:
                    return [UserModel(**user) for user in self.users]
            else:
                return []
        except Exception as error:
            print(error)
        
    def save_user(self):
        try:
            with open(USER_FILE, 'w') as file:
                users = [user.__dict__ for user in self.users]
                json.dump(users, file, indent=4)
        except Exception as error:
            print(error)