

from src.controllers.user_controller.user import make_admin, remove_user, get_all_user
from src.utility.validation import validate_email
from src.utility.check_user import check_user
from src.controllers.user_controller.user import get_user_by_email


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
    


