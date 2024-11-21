from src.database.collections.path import LOG_FILE
import os
import ast
# from datetime import datetime

# LOG_FILE = f'src/database/log/{datetime.now().strftime('%m-%Y')}.txt'

class Errors:
    def __init__(self):
        self.errors = self.load_error()

    def load_error(self):
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r') as file:
                err = file.read()
                # print(len(err.split('|')))
                error =err.split('|')
                result = []
                for err in error:
                    if len(err) == 0:
                        continue
                    else:
                        result.append(ast.literal_eval(err))
                return result
        else:
            return []
