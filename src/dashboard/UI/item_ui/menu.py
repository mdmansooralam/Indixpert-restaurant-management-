


from src.controllers.item_controller.item import get_item_by_category



def menu():
    print(f'*********************MENU************************\n')
    get_item_by_category('STARTER')

    get_item_by_category('MAIN COURSE')
    
    get_item_by_category('DRINK')

    get_item_by_category('ROTI')
