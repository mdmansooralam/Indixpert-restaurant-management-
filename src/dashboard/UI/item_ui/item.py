


from src.controllers.item_controller.item import create_item, remove_item, get_item_by_category, update_item
from src.utility.validation import validate_name, validate_price, validate_quantity, validate_id
from src.utility.check_item import check_item
from src.utility.verify_item_category import verify_item_category
from src.controllers.item_controller.item import add_stock
from src.utility.error_message import ErrorMessage
from src.database.collections.default import Default
from src.utility.get_input import get_input
from src.utility.log_error import LogError

def create():
    try:
        err_msg = ErrorMessage()
        name = get_input(validate_name, err_msg.enter_order_item, err_msg.invalid_order_item)
        if(not name):
            raise Exception(err_msg.invalid_order_item)
                    
        if(check_item(name)):
            raise Exception(err_msg.item_exist)
        
        display_category()    
        category = get_input(verify_item_category, err_msg.choose_option, err_msg.invalid_option)
        if(not category):
            raise Exception(err_msg.invalid_option)

        sale_price = take_item_price(category)
        if(not sale_price):
            raise Exception(err_msg.invalid_price)

        quantity = get_input(validate_quantity, err_msg.enter_quantity, err_msg.invalid_quantity)
        if(not quantity):
            raise Exception(err_msg.invalid_quantity)

        create_item(name, category, sale_price, quantity)

    except Exception as error:
        print(error)
        LogError().err.exception(error)

def delete():
    try:
        err_msg = ErrorMessage()
        id = get_input(validate_id, err_msg.enter_id, err_msg.invalid_id)
        if(not id):
            raise Exception(err_msg.invalid_id)
        
        remove_item(id)

    except Exception as error:
        print(error)
        LogError().err.exception(error)

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
        # id = validate_id(input('Enter Item Id : '))
        id = get_input(validate_id, err_msg.enter_id, err_msg.invalid_id)
        if(not id):
            raise Exception(err_msg.invalid_id)
        
        # name = validate_name(input('Enter item name : '))
        name = get_input(validate_name, err_msg.enter_item_name, err_msg.invalid_item)
        if(not name):
            raise Exception(err_msg.invalid_item)

        if(check_item(name)):
            raise Exception(err_msg.item_exist)

        display_category() 
        category = get_input(verify_item_category, err_msg.choose_option, err_msg.invalid_option)   
        # category = verify_item_category(input('Choose a option : '))
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
    try:
        err_msg = ErrorMessage()
        item_id = get_input(validate_id, err_msg.enter_id, err_msg.invalid_id)
        if(not item_id):
            raise Exception(err_msg.invalid_id)
        
        qty = get_input(validate_quantity, err_msg.enter_quantity, err_msg.invalid_quantity)
        if(not qty):
            raise Exception(err_msg.invalid_quantity)
    
        add_stock(item_id, qty)

    except Exception as error:
        print(error)
        LogError().err.exception(error)
    
def display_category():
    try:
        category_list = Default().item_category
        for category in category_list:
            print(f'{category['id']} : {category['name']}')

    except Exception as error:
        print(error)
        LogError().err.exception(error)
        
def take_item_price(category):
    try:
        err_msg = ErrorMessage()
        if(category == 'MAIN COURSE'):
            full_price = get_input(validate_price, "Enter full price : ", err_msg.invalid_price)
            if(not full_price):
                raise Exception(err_msg.invalid_price)
            
            half_price = get_input(validate_price, 'Half Price : ', err_msg.invalid_price)
            if(not half_price):
                raise Exception(err_msg.invalid_price)
            
            quarter_price = get_input(validate_price, 'Quarter Price : ', err_msg.invalid_price)
            if(not quarter_price):
                raise Exception(err_msg.invalid_price)
            
            sale_price = {
                "full_price": full_price,
                "half_price": half_price,
                "quarter_price": quarter_price
            }
            return sale_price

        elif(category == 'DRINK'or category == 'STARTER'):
            price = get_input(validate_price, 'Enter price : ', err_msg.invalid_price)
            if(not price):
                raise Exception(err_msg.invalid_price)
            return price
    except Exception as error:
        print(error)
        LogError().err.exception(error)