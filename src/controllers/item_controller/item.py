import uuid
import traceback
from src.controllers.user_controller.user_state import UserState
from src.models.item_model import ItemModel
from src.database.collections.item import Item
from src.utility.log_error import LogError, log
from src.utility.error_message import ErrorMessage
from src.utility.colors import bcolors

def create_item(name, category, sale_price, quantity):
    try:
        err_msg = ErrorMessage()
        ITEM = Item()
        id = str(uuid.uuid4())[:4].upper()
        added_by = UserState().get_state()['email']
        new_item = ItemModel(id, name, category, sale_price, quantity, added_by).__dict__
        ITEM.items.append(new_item)
        ITEM.save_item()
        print(err_msg.item_created)
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

def remove_item(id):
    try:
        err_msg = ErrorMessage()
        ITEM = Item()

        for item in ITEM.items:
            if(item['id'] == id):
                ITEM.items.remove(item)
                ITEM.save_item()
                print(f'{item['name']} {err_msg.item_removed}')
                break
        else:
            print(err_msg.item_not_found)
    except Exception as error:
        log(traceback.extract_tb(error.__traceback__)[0], error)
        print(error)

def get_item_by_category(category):
    try:

        if(category=='DRINK' or category== 'STARTER' or category == 'ROTI'):
            print(f'{bcolors.ENDC}\n{'='*33}{category}{'='*33}\n')
            items = Item().items
            fm_str = '{:<10}{:<10}{:<25}{:<20}'
            print(f'{bcolors.HEADER}{fm_str.format('S NO.','ID' ,'NAME', 'RATE')}')
            print('-'*65)
            items_count = 1
            for item in items:
                if(item['category'] == category):
                    print(f'{bcolors.OKBLUE}{fm_str.format(items_count, item['id'], item['name'], round(item['sale_price']))}')
                    items_count += 1
        else:
            print(f'{bcolors.ENDC}\n{'='*33}{category}{'='*33}\n')
            items = Item().items
            fm_str = '{:<10}{:<10}{:<25}{:<10}{:<10}{:<10}'
            print(f'{bcolors.HEADER}{fm_str.format('S NO.','ID', 'NAME', 'FULL', 'HALF', 'QUARTER')}')
            print('-'*75)
            items_count = 1
            for item in items:
                if(item['category'] == category):
                    print(f'{bcolors.OKBLUE}{fm_str.format(
                        items_count,
                        item['id'],
                        item['name'],
                        round(item['sale_price']['full_price']),
                        round(item['sale_price']['half_price']),
                        round(item['sale_price']['quarter_price']),
                    )}')
                    items_count += 1

    except Exception as error:
        log(traceback.extract_tb(error.__traceback__)[0], error)
        print(error)

def get_all_items():
    try:
        err_msg = ErrorMessage()
        items = Item().items
        user_state = UserState().get_state()
        if(user_state['role'] == 'admin'):
            fmt_str = '{:<20}{:<20}{:<10}'
            print(fmt_str.format('ID', 'NAME', 'STOCK'))
            print('-'*50)
            for item in items:
                print(fmt_str.format(item['id'], item['name'], item['quantity']))
        else:
            print(err_msg.not_authorized)
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

def add_stock(item_id, qty):
    try:
        err_msg = ErrorMessage()
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
                print(err_msg.item_not_found)
        else:
            print(err_msg.not_authorized)
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

def view_stock():
    try:
        err_msg = ErrorMessage()
        items = Item().items
        user_state = UserState().get_state()
        if(user_state['role'] == 'admin'):
            fmt_str = '{:<20}{:<30}{:<10}'
            print(fmt_str.format('ID', 'NAME', 'STOCK'))
            print('-'*50)
            for item in items:
                print(fmt_str.format(item['id'], item['name'], item['quantity']))
        else:
            print(err_msg.not_authorized)
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)

def update_item(id, category, sale_price, quantity):
    try:
        err_msg = ErrorMessage()
        ITEM = Item()
        if(UserState().get_state()['role'] == 'admin'):
            for item in ITEM.items:
                if(item['id'] == id):
                    item['category'] = category
                    item['sale_price'] = sale_price
                    item['quantity'] = quantity
                    ITEM.save_item()
                    print(err_msg.item_updated)
                    return
            raise Exception(err_msg.item_not_found)
        else:
            print(err_msg.not_authorized)
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)