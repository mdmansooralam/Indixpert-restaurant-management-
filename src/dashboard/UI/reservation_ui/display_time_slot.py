
from src.database.collections.default import Default
from src.utility.log_error import LogError
from src.utility.colors import bcolors



def display_time_slot():
    try:
        time_slot = Default().time_slot
        fmt_str = '{:<5}{:<25}'
        if(time_slot):
            print(f'{bcolors.HEADER}{fmt_str.format('ID', 'TIME SLOT')}')
            for ts in time_slot:
                print(f'{bcolors.OKBLUE}{fmt_str.format(ts['id'], ts['slot'])}')
    except Exception as error:
        print(f'{bcolors.FAIL}{error}')
        LogError().err.exception(error)

