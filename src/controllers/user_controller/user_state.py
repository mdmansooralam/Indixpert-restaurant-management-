

USER_STATE = None

class UserState:
    def __init__(self):
        self.__user = self.load_state()

    def load_state(self):
        return USER_STATE
    
    def get_state(self):
        return self.__user
    
    def update_state(self, user):
        global USER_STATE
        USER_STATE = user
