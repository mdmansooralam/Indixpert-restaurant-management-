
from src.database.collections.default import Default



def display_time_slot():
    time_slot = Default().time_slot
    if(time_slot):
        print('{:<5}{:<25}'.format('ID', 'TIME SLOT'))
        for ts in time_slot:
            print('{:<5}{:<25}'.format(ts['id'], ts['slot']))

