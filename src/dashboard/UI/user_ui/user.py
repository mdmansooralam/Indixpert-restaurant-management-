

from src.controllers.user_controller.user import make_admin, remove_user, get_all_user, make_staff
from src.utility.validation import validate_email
from src.utility.check_user import check_user
from src.controllers.user_controller.user import get_user_by_email, update_user
from src.utility.validation import validate_name, validate_password, validate_dob, validate_mobile


def admin():
        try:
            email = validate_email(input('Enter Email : '))
            if(not email):
                raise Exception('please enter a valid email')
            if(not check_user(email)):
                raise Exception('user not found with this email')
            
            print(f'1 YES \n2 NO')
            print('Do you want to make admin')

            choice = int(input('choose option : '))

            if(choice == 1):
                make_admin(email)

            elif(choice == 2):
                print('cancelled')
                
            else:
                print('you choosed a wrong option')

        except Exception as error:
             print(error)

def staff():
        try:
            email = validate_email(input('Enter Email : '))
            if(not email):
                raise Exception('please enter a valid email')
            if(not check_user(email)):
                raise Exception('user not found with this email')
            
            print(f'1 YES \n2 NO')
            print('Do you want to make staff')

            choice = int(input('choose option : '))

            if(choice == 1):
                make_staff(email)

            elif(choice == 2):
                print('cancelled')
                
            else:
                print('you choosed a wrong option')

        except Exception as error:
             print(error)

def remove():
    try:
        email = validate_email(input('Enter Email : '))
        if(not email):
            raise Exception('please enter a valid email')
        if(not check_user(email)):
            raise Exception('user not found ')
        remove_user(email)

    except Exception as error:
        print(error)

def view_all_user():
    get_all_user()

def display_staff_profile():
    try:
        email = validate_email(input('Enter Email Id : '))
        if(not email):
            raise Exception('Invalid email please enter a valid email')
        get_user_by_email(email)

    except Exception as error:
        print(error)
    
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