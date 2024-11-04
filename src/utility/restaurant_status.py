



from src.constant import RESTAURANT_STATUS

def restaurant_status():
    if(RESTAURANT_STATUS == 'open'):
        return True
    else:
        print('Restaurant is close.....')
        return False