

from src.utility.validation import validate_int

def ask_for_dashboard(opt='Logout'):
    while True:
        choice = validate_int(input(f'\n1 Go Dashboard | 2 {opt} : '))
        if(not choice):
            print('please choose a valid option')
        else:
            if(choice == 1):
                return True
            elif(choice == 2):
                return False
            else:
                print('please choose 1 or 2')