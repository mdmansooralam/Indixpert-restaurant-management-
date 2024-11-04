





from src.controllers.reservation_controller.reservation import reserved_table
from src.utility.validation import validate_name, validate_int
from src.utility.validate_date import validate_date
from src.utility.time_slot import validate_time_slot
from src.dashboard.UI.reservation_ui.display_time_slot import display_time_slot

def table_reserve():
    try:
        name = validate_name(input('Name : '))
        if(not name):
            raise Exception('please enter a valid name')
        date = validate_date(input('Date ( DD-MM-YYYY ) : '))
        if(not date):
            raise Exception('please enter a valid date (DD-MM-YYYY)')
        
        display_time_slot()
        time_slot = validate_time_slot(input('Time slot : '))
        if(not time_slot):
            raise Exception('please enter a valid time slot from time slot')
        persons = validate_int(input('Persons : '))
        if(not persons):
            print('please enter a valid number of persons')


        reserved_table(name, date, time_slot, persons)
    except Exception as error:
        print(error)