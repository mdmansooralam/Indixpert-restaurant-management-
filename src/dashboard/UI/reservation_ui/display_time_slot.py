
from src.database.collections.default import Default
from src.utility.log_error import LogError



def display_time_slot():
    try:
        time_slot = Default().time_slot
        fmt_str = '{:<5}{:<25}'
        if(time_slot):
            print(fmt_str.format('ID', 'TIME SLOT'))
            for ts in time_slot:
                print(fmt_str.format(ts['id'], ts['slot']))
    except Exception as error:
        print(error)
        LogError().err.exception(error)

