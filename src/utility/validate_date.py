




from datetime import datetime


def validate_date(date):
    today = datetime.today().strftime('%d-%m-%Y')
    
    d = datetime.strptime(date, '%d-%m-%Y').strftime('%d-%m-%Y')

    if(today == d):
        return str(d)
    else:
        return False
