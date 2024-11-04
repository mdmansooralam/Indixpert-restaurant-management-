




from src.controllers.reservation_controller.reservation import cancel_reservaiton
from src.utility.validation import validate_id

def cancel():
    try:
        id = validate_id(input('Enter Reservation ID : '))
        if(not id):
            raise Exception('please enter a valid id')
        cancel_reservaiton(id)

    except Exception as error:
        print(error)