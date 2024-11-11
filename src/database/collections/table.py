import os
import json

from src.database.collections.path import TABLE_FILE
from src.utility.log_error import LogError

class Table:
    def __init__(self):
        self.tables = self.load_table()

    def load_table(self):
        try:
            if os.path.exists(TABLE_FILE):
                with open(TABLE_FILE, 'r') as file:
                    return json.load(file)
            else:
                return []
        except Exception as error:
            print(error)
            LogError().err.exception(error)

    def save_table(self):
        try:
            with open(TABLE_FILE, 'w') as file:
                tables = [table for table in self.tables]
                json.dump(tables, file, indent=4)
        except Exception as error:
            print(error)
            LogError().err.exception(error)