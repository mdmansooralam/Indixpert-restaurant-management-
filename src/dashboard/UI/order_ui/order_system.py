


from src.controllers.order_controller.take_order import take_order
from src.controllers.order_controller.save_order import finalize_order
from src.controllers.order_controller.review_order import review_order

from src.utility.validation import validate_name


def order_system():
    order = take_order()

    while True:
            action = validate_name(input(f'would you like to "add", "review" or "finalize" ("exit" for quit)\n'))
            if(not action):
                 print('please enter a valid option ')
            else:
                if(action == 'exit'):
                    print('Thank You !')
                    break

                elif(action == 'add'):
                    order.extend(take_order())

                elif(action == 'review'):
                    review_order(order)

                elif(action == 'finalize'):
                    finalize_order(order)
                    break
                    
                else:
                    print('Invalid input please try again .')