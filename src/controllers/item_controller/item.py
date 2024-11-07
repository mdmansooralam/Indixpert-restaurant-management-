import uuid

from src.controllers.user_controller.user_state import UserState
from src.models.item_model import ItemModel
from src.database.collections.item import Item

def create_item(name, category, sale_price, quantity):
    try:
        ITEM = Item()
        id = str(uuid.uuid4())[:4].upper()
        added_by = UserState().get_state()['email']
        new_item = ItemModel(id, name, category, sale_price, quantity, added_by).__dict__
        ITEM.items.append(new_item)
        ITEM.save_item()
        print('item created successful')
    except Exception as errro:
        print(errro)

def remove_item(id):
    try:
        ITEM = Item()

        for item in ITEM.items:
            if(item['id'] == id):
                ITEM.items.remove(item)
                ITEM.save_item()
                print(f'{item['name']} removed successful')
                break
        else:
            print('item not found ')
    except Exception as error:
        print(error)

def get_item_by_category(category):
    try:
        print(f'\n**************{category}************\n')
        items = Item().items
        print('{:<10}{:<20}{:<20}'.format('S NO.', 'NAME', 'RATE'))
        print('-'*40)
        items_count = 1
        for item in items:
            if(item['category'] == category):
                print('{:<10}{:<20}{:<20}'.format(items_count, item['name'], item['sale_price']))
                items_count += 1
    except Exception as error:
        print(error)

def get_all_items():
    items = Item().items
    user_state = UserState().get_state()
    if(user_state['role'] == 'admin'):
        print('{:<20}{:<20}{:<10}'.format('ID', 'NAME', 'STOCK'))
        print('-'*50)
        for item in items:
            print('{:<20}{:<20}{:<10}'.format(item['id'], item['name'], item['quantity']))
    else:
        print('you are not authorized')

def add_stock(item_id, qty):
    ITEM = Item()
    user_state = UserState().get_state()

    if(user_state['role'] == 'admin'):

        for item in ITEM.items:
            if(item['id'] == item_id):
                item['quantity'] += qty
                ITEM.save_item()
                print('stock added')
                return
        else:
            print('item not found')
    else:
        print('You are not authorized')

def view_stock():
    items = Item().items
    user_state = UserState().get_state()
    if(user_state['role'] == 'admin'):
        print('{:<20}{:<20}{:<10}'.format('ID', 'NAME', 'STOCK'))
        print('-'*50)
        for item in items:
            print('{:<20}{:<20}{:<10}'.format(item['id'], item['name'], item['quantity']))
    else:
        print('you are not authorized')

def update_item(id, name, category, sale_price, quantity):

    ITEM = Item()
    if(UserState().get_state()['role'] == 'admin'):
        for item in ITEM.items:
            if(item['id'] == id):
                item['name'] = name
                item['category'] = category
                item['sale_price'] = sale_price
                item['quantity'] = quantity
                ITEM.save_item()
                print('item updated successful')
                break
    else:
        print('you are not authorized')