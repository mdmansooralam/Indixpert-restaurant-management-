import os
import json


from src.database.collections.path import ORDER_FILE
from src.utility.log_error import LogError

class Order:
    def __init__(self):
        self.orders = self.load_order()

    def load_order(self):
        try:
            if os.path.exists(ORDER_FILE):
                with open(ORDER_FILE, 'r') as file:
                    return json.load(file)

            else:
                return []
        except Exception as error:
            print(error)
            LogError().err.exception(error)


    def save_order(self):
        try:
            with open(ORDER_FILE, 'w') as file:
                orders = [order for order in self.orders]
                json.dump(orders, file, indent=4)
        except Exception as error:
            print(error)
            LogError().err.exception(error)