import os
import json

from src.database.collections.path import DEFAULT_FILE

class Default:
    def __init__(self):
        self.__default = self.load_default()

    def load_default(self):
        try:
            if(os.path.exists(DEFAULT_FILE)):
                with open(DEFAULT_FILE, 'r') as file:
                    return json.load(file)
            else:
                return {}
        except Exception as error:
            print(f'{error} error from Default :: load_default')
    
    def save_default(self):
        try:
            with open(DEFAULT_FILE, 'w') as file:
                default = self.__default
                json.dump(default, file, indent=4)
        except Exception as error:
            print(f'{error} error form Default :: save_default')

    @property
    def role(self):
        return self.__default['role']
    
    @property
    def salary(self):
        return self.__default['salary']
    
    @property
    def tax_percent(self):
        return self.__default['tax_percent']
    
    @property
    def restaurant_status(self):
        return self.__default['restaurant_status']
    
    @property
    def employment_type(self):
        return self.__default['employment_type']
    
    @property
    def shift_preferences(self):
        return self.__default['shift_preferences']
    
    @property
    def benefits(self):
        return self.__default['benefits']
    
    @property
    def user_status(self):
        return self.__default['user_status']
    
    @property
    def time_slot(self):
        return self.__default['time_slot']
    
    @property
    def item_category(self):
        return self.__default['item_category']