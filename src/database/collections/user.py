import os
import json

from src.database.collections.path import USER_FILE
from src.utility.log_error import LogError

class User:
    def __init__(self):
        self.users = self.load_user()

    def load_user(self):
        try:
            if(os.path.exists(USER_FILE)):
                with open(USER_FILE, 'r') as file:
                    return json.load(file)
            else:
                return []
        except Exception as error:
            print(error)
            LogError().err.exception(error)
        
    def save_user(self):
        try:
            with open(USER_FILE, 'w') as file:
                users = [user for user in self.users]
                json.dump(users, file, indent=4)
        except Exception as error:
            print(error)
            LogError().err.exception(error)

            