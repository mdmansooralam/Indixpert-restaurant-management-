


from src.dashboard.UI.auth_ui.auth import login, signup
from src.utility.validation import validate_int

def authentication():

    while True:
        print('**********USER AUTHENTICATION***********')
        print('1 LOGIN')
        print('2 SIGNUP')
        print('3 EXIT')


        choice = validate_int(input('choose a option : '))
        if(not choice):
            print('please choose valid option')
            continue

        if(choice == 1):
            login()
        elif(choice == 2):
            signup()
        elif(choice == 3):
            break
        else:
            print('Please choose a valid option')
