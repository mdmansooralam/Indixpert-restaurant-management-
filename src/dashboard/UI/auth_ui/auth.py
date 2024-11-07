
from src.controllers.auth_controller.auth import user_login, user_signup
from src.utility.validation import validate_email, validate_password, validate_name, validate_mobile, validate_dob
from src.utility.log_error import log_error

def login():    
        try:
            email = validate_email(input('Enter Email : '))
            if(not email):
                 raise Exception('Please Enter a valid Email')
            
            password = validate_password(input('Enter Password : '))
            if(not password):
                 raise Exception('please enter a valid password')
            
            user_login(email, password)
        except Exception as error:
            log_error(error, 'from auth :: login')
            print(error)

def signup():
     try:
          name = validate_name(input('Enter Your Name : '))
          if(not name):
               raise Exception('please enter a valid name')
          gender = input('Gender (Male / Female) :')
          if(not (gender.lower() == 'male' or gender.lower() == 'female')):
               raise Exception('Invalid gender ')
            
          email = validate_email(input('Enter Your Email : '))
          if(not email):
               raise Exception('Please enter a valid email')
            
          password = validate_password(input('Create Password : '))
          if(not password):
               raise Exception('please enter a valid password')
            
          date_of_birth = validate_dob(input('Date of Birth (dd-mm-yyyy) : '))
          if(not date_of_birth):
               raise Exception('invalid date, age should be 18 or above')

          mobile_number = validate_mobile(input('Mobile Number : '))
          if(not mobile_number):
               raise Exception('Invalid Mobile Number')
            
          address = input('Address : ')
          if(len(address) <4):
               raise Exception('Invalid address please enter a valid address')

          user_signup(name, email, password, date_of_birth, mobile_number, address, gender)

     except Exception as error:
          print(error)