from datetime import datetime

def verify_time_slot(time_slot):
    current_time = datetime.strptime(datetime.now().strftime("%H:%M"), "%H:%M").time()

    slot_time = time_slot[:5]

    if(time_slot[6:8] == 'PM' and int(slot_time[:2]) <12):
        slot_time = f'{int(time_slot[:2]) + 12}:{time_slot[3:5]}'

    slot_time = datetime.strptime(slot_time, '%H:%M').time()

    if(current_time <= slot_time):
        return time_slot
    else:
        return False
