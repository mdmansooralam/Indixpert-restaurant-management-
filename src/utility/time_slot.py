





TIME_SLOT = ['10-11AM', '10-11 AM', '11-12 PM', '12-01 PM', '01-02 PM']
def validate_time_slot(time_slot):
    if(time_slot in TIME_SLOT):
        return time_slot
