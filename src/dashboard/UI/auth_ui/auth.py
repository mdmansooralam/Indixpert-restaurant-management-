
from src.controllers.auth_controller.auth import user_login, user_signup
from src.utility.validation import validate_email, validate_password, validate_name

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
            print(error)

def signup():
        try:
            name = validate_name(input('Enter Your Name : '))
            if(not name):
                 raise Exception('please enter a valid name')
            
            email = validate_email(input('Enter Your Email : '))
            if(not email):
                 raise Exception('Please enter a valid email')
            
            password = validate_password(input('Create Password : '))
            if(not password):
                 raise Exception('please enter a valid password')
            
            user_signup(name, email, password)

        except Exception as error:
            print(password)