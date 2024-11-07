

from src.utility.get_item import get_item
from src.utility.validation import validate_name, validate_quantity
from src.utility.error_message import ErrorMessage

def take_order():
    try:
        err_msg = ErrorMessage()
        order = []
        while True:
                choice = validate_name(input('Enter the Item that you like to order ("Done" to finish) : '))
                if(not choice):
                    print(err_msg.invalid_item)
                    continue
                        
                if choice == 'done':
                    break

                item = get_item(choice)
                if(item):
                    if(item['category'] == 'DRINK'):
                        quantity = validate_quantity(input(f'how many {choice} would you like : '))
                        if(not quantity):
                            print(err_msg.invalid_quantity)
                            continue
                    else:
                        pass
                    if(item['quantity'] >= quantity):
                            item['quantity'] = quantity
                            order.append(item)
                            print(f'{item['name']} added to your order')
                                    
                    else:
                            print(f'Only {item['quantity']} {item['name']} available')
                else:
                    print(f'Sorry we do not have {choice} in menu')

        return order
    except Exception as error:
        print(error)

