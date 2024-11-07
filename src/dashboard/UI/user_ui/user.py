

from src.controllers.user_controller.user import update_user
from src.utility.validation import validate_name, validate_dob, validate_mobile

    
def update_user_profile():
    try:
        name = validate_name(input('Enter Your Name : '))
        if(not name):
            raise Exception('please enter a valid name')
        gender = input('Gender (Male / Female) :')
        if(not (gender.lower() == 'male' or gender.lower() == 'female')):
            raise Exception('Invalid gender ')
    
        date_of_birth = validate_dob(input('Date of Birth (dd-mm-yyyy) : '))
        if(not date_of_birth):
            raise Exception('invalid date, age should be 18 or above')

        mobile_number = validate_mobile(input('Mobile Number : '))
        if(not mobile_number):
            raise Exception('Invalid Mobile Number')
            
        address = input('Address : ')
        if(len(address) <4):
            raise Exception('Invalid address please enter a valid address')

        update_user(name, date_of_birth, mobile_number, address, gender)

    except Exception as error:
          print(error)