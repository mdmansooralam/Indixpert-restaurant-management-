import os
import json

ITEM_FILE = 'src/database/items.json'

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
            print(f'{error} error from Item :: load_item')
    
    def save_item(self):
        try:
            with open(ITEM_FILE, 'w') as file:
                items = [item for item in self.items]
                json.dump(items, file, indent=4)
        except Exception as error:
            print(f'{error} error form Item :: save_item')