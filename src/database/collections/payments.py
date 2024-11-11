import os
import json

from src.database.collections.path import PAYMENT_FILE
from src.utility.log_error import LogError

class Payment:
    def __init__(self):
        self.payments = self.load_payment()

    def load_payment(self):
        try:
            if(os.path.exists(PAYMENT_FILE)):
                with open(PAYMENT_FILE, 'r') as file:
                    return json.load(file)
            else:
                return []
        except Exception as error:
            print(error)
            LogError().err.exception(error)
    
    def save_payment(self):
        try:
            with open(PAYMENT_FILE, 'w') as file:
                payments = [payment for payment in self.payments]
                json.dump(payments, file, indent=4)
        except Exception as error:
            print(error)
            LogError().err.exception(error)