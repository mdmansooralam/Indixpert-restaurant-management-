import uuid 
from datetime import datetime

from src.models.reservation_model import ReservationModel
from src.database.collections.reservation import Reservation
from src.database.collections.table import Table
from src.utility.validation import validate_id, validate_int
from src.database.collections.default import Default
from src.utility.error_message import ErrorMessage
from src.utility.log_error import LogError, log
from src.utility.get_input import get_input
from src.utility.time_slot import validate_time_slot_id
from src.dashboard.UI.reservation_ui.display_time_slot import display_time_slot
from src.utility.colors import bcolors
import traceback


def find_table(time_slot, persons):
    try:
        reservations = Reservation().reservations
        date = str(datetime.today().strftime("%d-%m-%Y"))
        tables = Table().tables
        reserved_table = [res['table_id'] for res in reservations if res['date'] == date and res['time_slot'] == time_slot and res['status'] == 'reserved']
        for table in tables:
            if table['seating_capacity'] >= persons and table['id'] not in reserved_table:
                return table
        return None
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

def reserved_table(name, mobile_no, time_slot, persons):
    try:
        err_msg = ErrorMessage()
        RESERVATION = Reservation()
        date = str(datetime.today().strftime("%d-%m-%Y"))
        table = find_table(time_slot, persons)
        if(not table):
            print(f'{bcolors.WARNING}{err_msg.table_not_available}')
        elif(table):
            id = str(uuid.uuid4())[:4].upper()
            status = 'reserved'
            new_reservation = ReservationModel(id, table['id'], date, time_slot, persons, name, mobile_no, status).__dict__
            RESERVATION.reservations.append(new_reservation)
            RESERVATION.save_reservation()
            print(f'{bcolors.OKGREEN}table reserved successful table Id : {table['id']} reservation id : {new_reservation['id']}')
            return True
    except Exception as error:
        print(f'{bcolors.FAIL}{error}')
        log(traceback.extract_tb(error.__traceback__)[0], error)

def cancel_reservaiton(id):
    try:
        err_msg = ErrorMessage()
        RESERVATION = Reservation()

        for res in RESERVATION.reservations:
            if(res['id'] == id):
                if(res['status'] == 'reserved'):
                    res['status'] = 'cancelled'
                    RESERVATION.save_reservation()
                    print(f'{bcolors.OKGREEN}{err_msg.reservation_canceled}')
                    return
                else:
                    print(f'{bcolors.FAIL}{err_msg.reservation_already_cancel}')
                    return
        else:
            print(f'{bcolors.FAIL}{err_msg.reservation_not_found}')
    except Exception as error:
        print(f'{bcolors.FAIL}{error}')
        log(traceback.extract_tb(error.__traceback__)[0], error)

def get_reservation():
    try:
        err_msg = ErrorMessage()
        reservations = Reservation().reservations

        id = get_input(validate_id, err_msg.enter_id, err_msg.invalid_id)
        if(not id):
            raise Exception(err_msg.invalid_id)
        fmt_str = '{:<10}{:<20}{:<10}{:<10}{:<10}{:<15}{:<15}'
        for res in reservations:
            if(res['id'] == id):
                print(fmt_str.format('ID','NAME','TABLE ID','PERSONS', 'STATUS', 'DATE', 'TIME SLOT'))
                print(fmt_str.format(
                    res['id'],
                    res['name'],
                    res['table_id'],
                    res['persons'],
                    res['status'],
                    res['date'],
                    res['time_slot']
                    ))
                return
        else:
            print(err_msg.reservation_not_found)
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

def get_all_reservaiton():
    try:
        err_msg = ErrorMessage()
        reservations = Reservation().reservations
        fmt_str = '{:<10}{:<20}{:<10}{:<10}{:<10}{:<15}{:<15}'
        if(reservations):
            print(fmt_str.format('ID','NAME','TABLE ID','PERSONS', 'STATUS', 'DATE', 'TIME SLOT'))
            for res in reservations:
                print(fmt_str.format(
                    res['id'],
                    res['name'],
                    res['table_id'],
                    res['persons'],
                    res['status'],
                    res['date'],
                    res['time_slot']
                    ))
        else:
            print(err_msg.reservation_not_found)
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)
    
def auto_reserve(name, mobile_no, persons):
    try:
        time = str(datetime.now().strftime('%H:%M'))
        #checking for slot
        time_slots = Default().time_slot
        for time_slot in time_slots:
            slot_time = time_slot["slot"][:5]
            
            if(time_slot['slot'][6:8] == 'PM' and int(slot_time[:2]) <12):
                slot_time = f'{int(time_slot["slot"][:2]) + 12}:{time_slot["slot"][3:5]}'

            if(datetime.strptime(time, "%H:%M") <= datetime.strptime(slot_time, "%H:%M")):
                res = reserved_table(name, mobile_no, time_slot['slot'], persons)
                if(res):
                    return True
                else:
                    return False
    except Exception as error:
        log(traceback.extract_tb(error.__traceback__)[0], error)
        return False

def get_available_table():
    try:
        err_msg = ErrorMessage()
        display_time_slot()
        time_slot = get_input(validate_time_slot_id, err_msg.choose_option, err_msg.invalid_option)
        if(not time_slot):
            raise Exception(err_msg.invalid_option)
        
        persons = get_input(validate_int, err_msg.number_of_person, err_msg.invalid_number_of_person)
        if(not persons):
            raise Exception(err_msg.invalid_number_of_person)

        reservations = Reservation().reservations
        date = str(datetime.today().strftime("%d-%m-%Y"))
        tables = Table().tables
        reserved_table = [res['table_id'] for res in reservations if res['date'] == date and res['time_slot'] == time_slot and res['status'] == 'reserved']

        fmt_str = '{:<10}{:<20}'
        print(fmt_str.format('Table Id', 'Capacity'))
        for table in tables:
            if table['seating_capacity'] >= persons and table['id'] not in reserved_table:
                print(fmt_str.format(table['id'], table['seating_capacity']))
                
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

