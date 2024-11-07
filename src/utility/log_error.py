
import os
from src.database.collections.path import LOG_FILE

def log_error(msg, source):
    try:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'a') as file:
                error_msg = f'\n{msg}|{source}'
                file.write(error_msg)
        else:
            with open(LOG_FILE, 'w') as file:
                error_msg = f'{msg}|{source}'
                file.write(error_msg)
    except Exception as error:
        print(error)


