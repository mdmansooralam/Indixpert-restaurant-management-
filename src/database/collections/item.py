import os
import json
import traceback
from src.database.collections.path import ITEM_FILE
from src.utility.log_error import LogError, log

class Item:
    def __init__(self):
        self.items = self.load_item()

    def load_item(self):
        try:
            if(os.path.exists(ITEM_FILE)):
                with open(ITEM_FILE, 'r') as file:
                    return json.load(file)
            else:
                return []
        except Exception as error:
            print(error)
            log(traceback.extract_tb(error.__traceback__)[0], error)
    
    def save_item(self):
        try:
            with open(ITEM_FILE, 'w') as file:
                items = [item for item in self.items]
                json.dump(items, file, indent=4)
        except Exception as error:
            print(error)
            log(traceback.extract_tb(error.__traceback__)[0], error)