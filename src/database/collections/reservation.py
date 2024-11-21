import os
import json
import traceback
from src.database.collections.path import RESERVATION_FILE
from src.utility.log_error import LogError, log

class Reservation:
    def __init__(self):
        self.reservations = self.load_reservation()

    def load_reservation(self):
        try:
            if os.path.exists(RESERVATION_FILE):
                with open(RESERVATION_FILE, 'r') as file:
                    return json.load(file)
            else:
                return []
        except Exception as error:
            print(error)
            log(traceback.extract_tb(error.__traceback__)[0], error)

    def save_reservation(self):
        try:
            with open(RESERVATION_FILE, 'w') as file:
                reservations = [res for res in self.reservations]
                json.dump(reservations, file, indent=4)
                
        except Exception as error:
            print(error)
            log(traceback.extract_tb(error.__traceback__)[0], error)