
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
        


import traceback
import datetime


# f = 'err.txt'
# email = 'mansooralam@gmail.com'
# date_time = datetime.now()
# print(date_time)

# def log_error(tb, msg=None):
#     d = {}
#     d['date_time'] = str(date_time)
#     d['email'] = email
#     d['path'] = tb[0]
#     d['line'] = tb[1]
#     d['fun_name'] = tb[2]
#     d['err'] = tb[3]
#     d['msg'] = msg

#     result = f'\n|{str(d)}:'
#     with open(filename, 'a') as file:
#         file.write(result)
        



