
from src.database.collections.item import Item

def get_item(name):
    for item in Item().items:
        if(item['name'] == name or item['id'] == name.upper()):
            return item
    else:
        return False