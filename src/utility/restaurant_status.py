

from src.database.collections.default import Default

def restaurant_status():
    if(Default().restaurant_status == 'open'):
        return True
    else:
        print('Restaurant is close.....')
        return False