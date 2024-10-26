
from src.manage_files.item import Item

def get_item(name):
    for item in Item().items:
        if(item['name'] == name):
            return item
    else:
        return False