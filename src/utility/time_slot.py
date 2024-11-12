


from src.database.collections.default import Default
from src.utility.verify_time_slot  import verify_time_slot


def validate_time_slot_id(time_slot_id):
    try:
        time_slot = Default().time_slot
        if(time_slot):
            for ts in time_slot:
                if(ts['id'] == int(time_slot_id)):
                    # return ts['slot']
                    if(verify_time_slot(ts['slot'])):
                        return ts['slot']
                    else:
                        print('Please choose a correct time slot')

        else:
            print('some internal issue in time slot')
            return False
    except:
        return False

