


from src.controllers.order_controller.order import take_order
from src.controllers.order_controller.order import finalize_order
from src.controllers.order_controller.order import review_order
from src.controllers.order_controller.order import payment_proceed

from src.utility.validation import validate_name


def order_system():
    order = take_order()

    while True:
            action = validate_name(input(f'would you like to "add", "review", "save" or "billing" ("exit" for quit)\n'))
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

                elif(action == 'save'):
                    finalize_order(order)
                    break
                elif(action == 'billing'):
                    order_id = finalize_order(order)
                    payment_proceed(order_id)
                    break
                    
                else:
                    print('Invalid input please try again .')