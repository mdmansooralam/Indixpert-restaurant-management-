

from src.manage_files.item import Item

def check_item(name):
    item_found = False
    for item in Item().items:
        if(item['name'] ==  name):
            item_found = True
            return True
    else:
        if(not item_found):
            return False
        