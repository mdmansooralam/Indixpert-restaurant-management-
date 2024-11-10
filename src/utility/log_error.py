
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
            format=f'||{self.email if self.email else 'auth time'} \n {"%(asctime)s"} {"%(message)s"}')
        



