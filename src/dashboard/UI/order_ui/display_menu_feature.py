

from src.database.collections.item import Item


def display_menu():
    try:
        print('\n')
        print('{:<20}{:<20}{:<10}'.format('NAME','CATEGORY', 'RATE'))
        print('-'*50)
        items = Item().items
        for item in items:
            print('{:<20}{:<20}{:<10}'.format(item['name'], item['category'], item['sale_price']))
            
    except Exception as error:
        print(error)
