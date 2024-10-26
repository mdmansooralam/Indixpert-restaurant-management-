
from src.manage_files.item import Item

def check_quantity(name, quantity):
    item_found = False
    for item in Item().items:
        if(item['name'] == name and item['quantity'] >= quantity):
            item_found = True
            return item
    else:
        if(not item_found):
            return False
    
    
