






from src.database.collections.order import Order
from src.controllers.order_controller.take_order import take_order
from src.database.collections.item import Item
from src.utility.check_order import check_order
from src.controllers.order_controller.payment_proceed import payment_proceed
from src.utility.validation import validate_id
from src.utility.get_order import get_order
from src.constant import TAX


def update_order():
    id = validate_id(input('enter id :'))
    if(id):
        found_order = get_order(id)
        if(found_order['status'] == 'process'):
            ORDER = Order()
            ITEM = Item()
            new_items = take_order()
            total = 0

            if(new_items):
                for new_item in new_items:
                    for item in ITEM.items:
                        if(new_item['name'] == item['name']):
                            item['quantity'] -= new_item['quantity']
                            total += item['sale_price'] * new_item['quantity']
                            ITEM.save_item()
            
            for order in ORDER.orders:
                if(order['id'] == id):
                    order['items'].extend(new_items)
                    order['total'] += total
                    order['tax'] += total / 100 * TAX
                    order['grand_total'] = order['total'] + order['tax'] - order['discount']
                    ORDER.save_order()
                    break

            action = input('would you like to "save" or "pay" ')

            if(action == 'pay'):
                payment_proceed(id)
            else:
                print('your order has been saved and  in process')
        else:
            print('order already completed now you cannot update')
    else:
        print('please enter a valid order id')







