





from src.controllers.reservation_controller.reservation import reserved_table
from src.utility.validation import validate_name, validate_int, validate_mobile
from src.utility.validate_date import validate_date
from src.utility.time_slot import validate_time_slot_id
from src.dashboard.UI.reservation_ui.display_time_slot import display_time_slot

def table_reserve():
    try:
        name = validate_name(input('Enter Name : '))
        if(not name):
            raise Exception('please enter a valid name')
        
        mobile_no = validate_mobile(input('Enter Mobile No :'))
        if(not mobile_no):
            raise Exception('please enter a valid mobile number')
        
        # date = validate_date(input('Date ( DD-MM-YYYY ) : '))
        # if(not date):
        #     raise Exception('please enter a valid date (DD-MM-YYYY)')
        
        display_time_slot()

        time_slot = validate_time_slot_id(input('Choose Time slot id : '))
        if(not time_slot):
            raise Exception('please choose valid time slot id : ')
        
        persons = validate_int(input('Persons : '))
        if(not persons):
            print('please enter a valid number of persons')


        reserved_table(name, mobile_no, time_slot, persons)
    except Exception as error:
        print(error)