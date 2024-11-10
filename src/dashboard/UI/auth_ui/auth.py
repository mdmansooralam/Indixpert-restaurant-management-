
from src.controllers.auth_controller.auth import user_login, user_signup
from src.utility.validation import validate_email, validate_password, validate_name, validate_mobile, validate_dob
from src.utility.log_error import LogError
from src.utility.error_message import ErrorMessage
from src.utility.get_input import get_input
def login():    
        try:
            err_msg = ErrorMessage()
            email = get_input(validate_email, err_msg.enter_email, err_msg.invalid_email)
            if(not email):
                 raise Exception(err_msg.invalid_email)
            
            password = get_input(validate_password, err_msg.enter_password, err_msg.invalid_password)
            if(not password):
                 raise Exception(err_msg.invalid_password)
            
            user_login(email, password)
        except Exception as error:
            LogError().err.exception(error)
            print(error)

def signup():
     try:
          err_msg = ErrorMessage()
          name = get_input(validate_name, err_msg.enter_name, err_msg.invalid_name)
          if(not name):
               raise Exception(err_msg.invalid_name)
          
          gender = input('Gender (Male / Female) :')
          if(not (gender.lower() == 'male' or gender.lower() == 'female')):
               raise Exception('Invalid gender ')
            
          email = get_input(validate_email, err_msg.enter_email, err_msg.invalid_email)
          if(not email):
               raise Exception(err_msg.invalid_email)
            
          password = get_input(validate_password, err_msg.invalid_password)
          if(not password):
               raise Exception(err_msg.invalid_password)
            
          date_of_birth = get_input(validate_dob, err_msg.enter_dob, err_msg.invalid_dob)
          if(not date_of_birth):
               raise Exception(err_msg.invalid_dob)

          mobile_number = get_input(validate_mobile, err_msg.enter_mobile_number, err_msg.invalid_mobile_number)
          if(not mobile_number):
               raise Exception(err_msg.invalid_mobile_number)
            
          address = input(err_msg.enter_address)
          if(len(address) <4):
               raise Exception(err_msg.invalid_address)

          user_signup(name, email, password, date_of_birth, mobile_number, address, gender)

     except Exception as error:
          print(error)