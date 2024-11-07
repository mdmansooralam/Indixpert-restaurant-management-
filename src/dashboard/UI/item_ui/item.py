


from src.controllers.item_controller.item import create_item, remove_item, get_item_by_category, update_item
from src.utility.validation import validate_name, validate_price, validate_quantity, validate_id
from src.utility.check_item import check_item
from src.utility.verify_item_category import verify_item_category
from src.controllers.item_controller.item import add_stock
from src.utility.error_message import ErrorMessage
from src.database.collections.default import Default

def create():
    try:
        err_msg = ErrorMessage()
        name = validate_name(input('Item Name : '))
        if(not name):
            raise Exception(err_msg.invalid_item)
                    
        if(check_item(name)):
            raise Exception(err_msg.item_exist)
        
        display_category()    
        category = verify_item_category(input('Choose a Option : '))
        if(not category):
            raise Exception(err_msg.invalid_option)

        sale_price = take_item_price(category)
        if(not sale_price):
            raise Exception(err_msg.invalid_price)

        quantity = validate_quantity(input('Quantity : '))
        if(not quantity):
            raise Exception(err_msg.invalid_quantity)

        create_item(name, category, sale_price, quantity)

    except Exception as error:
        print(error)

def delete():
    try:
        err_msg = ErrorMessage()
        id = validate_id(input('Enter item Id  : '))
        if(not id):
            raise Exception(err_msg.invalid_id)
        
        remove_item(id)

    except Exception as error:
        print(error)

def display_item_by_category():
    try:
        err_msg = ErrorMessage()
        display_category()
        category = verify_item_category(input('Choose a option : '))
        if(not category):
            raise Exception(err_msg.invalid_option)
        get_item_by_category(category)

    except Exception as error:
        print(error)

def update():
    try:
        err_msg = ErrorMessage()
        id = validate_id(input('Enter Item Id : '))
        if(not id):
            raise Exception(err_msg.invalid_id)
        
        name = validate_name(input('Enter item name : '))
        if(not name):
            raise Exception(err_msg.invalid_item)

        if(check_item(name)):
            raise Exception(err_msg.item_exist)

        display_category()    
        category = verify_item_category(input('Choose a option : '))
        if(not category):
            raise Exception(err_msg.invalid_option)

        sale_price = take_item_price(category)
        if(not sale_price):
            raise Exception(err_msg.invalid_price)

        quantity = validate_quantity(input('Quantity : '))
        if(not quantity):
            raise Exception(err_msg.invalid_quantity)
        
        update_item(id, name, category, sale_price, quantity)

    except Exception as error:
        print(error)

def stock():
    err_msg = ErrorMessage()
    item_id = validate_id(input('Item Id : '))
    if(not item_id):
        print(err_msg.invalid_id)
        return
    
    qty = validate_quantity(input('Quantity : '))
    if(not qty):
        print(err_msg.invalid_quantity)
        return
    
    add_stock(item_id, qty)

def display_category():
    try:
        category_list = Default().item_category
        for category in category_list:
            print(f'{category['id']} : {category['name']}')

    except Exception as error:
        print(error)
        
def take_item_price(category):
    if(category == 'MAIN COURSE'or category == 'STARTER'):
        full_price = validate_price(input('Full Price : '))
        if(not full_price):
            return 
        
        half_price = validate_price(input('Half Price : '))
        if(not half_price):
            return
        
        quarter_price = validate_price(input('Quarter Price : '))
        if(not quarter_price):
            return
        
        sale_price = {
            "full_price": full_price,
            "half_price": half_price,
            "quarter_price": quarter_price
        }
        return sale_price

    elif(category == 'DRINK'):
        price = validate_price(input('Price : '))
        if(not price):
            return
        return price