

from src.utility.get_item import get_item
from src.utility.validation import validate_name, validate_int

def take_order():
    try:

        order = []
        while True:
                choice = validate_name(input('Enter the Item that you like to order ("Done" to finish) : '))
                if(not choice):
                    print('please enter a valid option')
                        
                item = get_item(choice)

                if choice == 'done':
                    break

                elif(item):
                    quantity = validate_int(input(f'how many {choice} would you like : '))
                    if(not quantity):
                        print('please enter a valid quantity')
                    else:
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

