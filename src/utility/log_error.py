
from src.database.collections.path import LOG_FILE
import logging
from src.controllers.user_controller.user_state import UserState


class LogError:
    def __init__(self):
        self.email = UserState().get_state()['email'] if UserState().get_state() else None
        self.err = logging
        
        logging.basicConfig(
            filemode='a',
            filename=LOG_FILE,
            datefmt='%H:%M:%S',
            format=f'||{self.email if self.email else "auth time"} \n {"%(asctime)s"} {"%(message)s"}')
        

from datetime import datetime

def log(tb, msg=None):
    try:
        user = UserState().get_state()
        error = {
            "date_time" : f'{str(datetime.now())}',
            "email": f'{user['email'] if user else 'known'}',
            "path" : f'{tb[0]}',
            "line" : f'{tb[1]}',
            "fn_name" : f'{tb[2]}',
            "err": f'{tb[3]}',
            "msg" : f'{msg}'
        }

        result = f'|{str(error)}\n'
        with open(LOG_FILE, 'a') as file:
            file.write(result)
    except Exception as error:
        print(error)



