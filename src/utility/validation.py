import re
from datetime import datetime

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if(re.match(pattern, email)):
        return email.lower()
    else:
        return False
    
def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{7,}$'
    if(re.match(pattern, password)):
        return password
    else:
        return False
    
def validate_name(name):
    pattern = r"^[A-Za-z].*$"
    if(re.match(pattern, name)):
        return name.lower()
    else:
        return False
    
def validate_quantity(qty):
    pattern = r'^[1-9]\d*$'
    if(re.match(pattern, qty)):
        return int(qty)
    
def validate_price(price):
    pattern = r'^[1-9]\d*$'
    if(re.match(pattern, price)):
        return float(price)
    else:
        return False
    
def validate_category(category):
    if(category.upper() == 'MAIN COURSE' or category.upper() == 'STARTER' or category.upper() == 'DRINKS'):
        return category.upper()
    else:
        return False
    
def validate_id(id):
    pattern = r"^[A-Za-z0-9]{4}$"
    if(re.match(pattern, id)):
        return id.upper()
    else:
        return False
    
def validate_mobile(number):
    pattern = r'^(?!([0-9])\1{9})\d{10}$'
    if(re.match(pattern, number)):
        return number
    else:
        return False

def validate_int(number):
    pattern = r'^[1-9]\d*$'
    if(re.match(pattern, number)):
        return int(number)
    else:
        return False

def validate_dob(dob):
    try:
        current_year = datetime.today().year
        birth_year = datetime.strptime(dob, '%d-%m-%Y').year

        age = current_year - birth_year

        if(age >= 18 and age <=95):
            return dob
        else:
            return False
        

    except Exception as error:
        return False
