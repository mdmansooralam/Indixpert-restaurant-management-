


from src.controllers.item_controller.item import create_item, remove_item, get_item_by_category, update_item
from src.utility.validation import validate_name, validate_category, validate_price, validate_quantity, validate_id
from src.utility.check_item import check_item
from src.controllers.item_controller.item import add_stock


def create():
        try:
            name = validate_name(input('Item Name : '))
            if(not name):
                raise Exception('please enter a valid name')
            if(check_item(name)):
                raise Exception('item already in menu')
            
            category = validate_category(input('Item Category : '))
            if(not category):
                raise Exception('please enter a valid category')
            
            cost_price = validate_price(input('Cost Price : '))
            if(not cost_price):
                raise Exception('please enter a valid cost price')

            sale_price = validate_price(input('Sale Price : '))
            if(not sale_price):
                raise Exception('please enter a valide sale price')

            quantity = validate_quantity(input('Quantity : '))
            if(not quantity):
                raise Exception('please enter a valid quantity')

            create_item(name, category, cost_price, sale_price, quantity)
        
        except Exception as error:
            print(error)

def delete():
    try:
        id = validate_id(input('Enter item Id  : '))
        if(not id):
            raise Exception('please enter a valid id')
        
        remove_item(id)

    except Exception as error:
        print(error)

def display_item_by_category():
    try:
        category = validate_category(input('please enter category : '))
        if(not category):
            print('category not found ')
        else:
            get_item_by_category(category)

    except Exception as error:
        print(error)

def update():
    try:
        id = validate_id(input('Enter Id : '))
        if(not id):
            raise Exception('please enter a valid id')
        
        name = validate_name(input('Item Name : '))
        if(not name):
            raise Exception('please enter a valid name')
        if(check_item(name)):
            raise Exception('item already in menu')
            
        category = validate_category(input('Item Category : '))
        if(not category):
            raise Exception('please enter a valid category')
            
        cost_price = validate_price(input('Cost Price : '))
        if(not cost_price):
            raise Exception('please enter a valid cost price')

        sale_price = validate_price(input('Sale Price : '))
        if(not sale_price):
            raise Exception('please enter a valide sale price')

        quantity = validate_quantity(input('Quantity : '))
        if(not quantity):
            raise Exception('please enter a valid quantity')
        
        update_item(id, name, category, cost_price, sale_price, quantity)

    except Exception as error:
        print(error)

def stock():
    item_id = validate_id(input('Item Id : '))
    if(not item_id):
        print('Invalid item id ')
        return
    qty = validate_quantity(input('Quantity : '))
    if(not qty):
        print('Invalid quantity you entered')
        return
    
    add_stock(item_id, qty)
