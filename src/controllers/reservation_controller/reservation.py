import uuid 
from datetime import datetime

from src.models.reservation_model import ReservationModel
from src.database.collections.reservation import Reservation
from src.database.collections.table import Table
from src.utility.validation import validate_id
from src.database.collections.default import Default


def find_table(time_slot, persons):
    reservations = Reservation().reservations
    date = str(datetime.today().strftime("%d-%m-%Y"))
    tables = Table().tables
    reserved_table = [res['table_id'] for res in reservations if res['date'] == date and res['time_slot'] == time_slot and res['status'] == 'reserved']
    for table in tables:
        if table['seating_capacity'] >= persons and table['id'] not in reserved_table:
            return table
    return None

def reserved_table(name, mobile_no, time_slot, persons):
        RESERVATION = Reservation()
        date = str(datetime.today().strftime("%d-%m-%Y"))
        table = find_table(time_slot, persons)
        if(not table):
            print('table not available')
        elif(table):
            id = str(uuid.uuid4())[:4].upper()
            status = 'reserved'
            new_reservation = ReservationModel(id, table['id'], date, time_slot, persons, name, mobile_no, status).__dict__
            RESERVATION.reservations.append(new_reservation)
            RESERVATION.save_reservation()
            print(f'table reserved successful table Id : {table['id']} reservation id : {new_reservation['id']}')
            return True

def cancel_reservaiton(id):
    RESERVATION = Reservation()

    for res in RESERVATION.reservations:
        if(res['id'] == id):
            if(res['status'] == 'reserved'):
                res['status'] = 'cancelled'
                RESERVATION.save_reservation()
                print('Your reservation has been cancelled')
                return
            else:
                print('your reservation already cancelled')
                return
    else:
        print('reservation not found ')

def get_reservation():
    reservations = Reservation().reservations

    id = validate_id(input('Reservation Id : '))
    if(not id):
        print('please enter a valid id ')
        return

    for res in reservations:
        if(res['id'] == id):
            print('{:<10}{:<20}{:<10}{:<10}{:<10}{:<15}{:<15}'.format('ID','NAME','TABLE ID','PERSONS', 'STATUS', 'DATE', 'TIME SLOT'))
            print('{:<10}{:<20}{:<10}{:<10}{:<10}{:<15}{:<15}'.format(
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
        print('no reservation found')

def get_all_reservaiton():
    reservations = Reservation().reservations

    if(reservations):
        print('{:<10}{:<20}{:<10}{:<10}{:<10}{:<15}{:<15}'.format('ID','NAME','TABLE ID','PERSONS', 'STATUS', 'DATE', 'TIME SLOT'))
        for res in reservations:
            print('{:<10}{:<20}{:<10}{:<10}{:<10}{:<15}{:<15}'.format(
                res['id'],
                res['name'],
                res['table_id'],
                res['persons'],
                res['status'],
                res['date'],
                res['time_slot']
                ))
    else:
        print('no reservation found')
    
def auto_reserve(name, mobile_no, persons):
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



