import uuid
from datetime import date

from src.utility.get_item import get_item
from src.utility.validation import validate_name, validate_quantity, validate_mobile, validate_id
from src.utility.error_message import ErrorMessage
from src.utility.get_order import get_order
from src.utility.check_order import check_order

from src.controllers.user_controller.user_state import UserState
from src.controllers.payment_gateway_controller.payment_gateway import pay

from src.database.collections.order import Order
from src.database.collections.default import Default
from src.database.collections.item import Item

from src.models.order_model import OrderModel


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

def finalize_order(order):
    try:
        ORDER = Order()
        ITEM = Item()
        name = validate_name(input('Customer Name : '))
        if(not name):
            print('please enter a valid name')
            return
        
        mobile_no = validate_mobile(input('Customer Mobile Number : '))

        if(not mobile_no):
            print('please enter a valid mobile number')
            return
        else:
            total = 0
            if order:
                for order_item in order:
                    for item in ITEM.items:
                        if(item['name'] == order_item['name']):
                            item['quantity'] -= order_item['quantity']
                            #add total
                            total += item['sale_price'] * order_item['quantity']
                            ITEM.save_item()  

                id = str(uuid.uuid4())[:4].upper()
                order_date = date.today().strftime('%d-%m-%Y')
                create_by = UserState().get_state()['email']
                status = 'process'
                tax_percent = Default().tax_percent
                tax = round((total / 100 * tax_percent), 2)
                discount = 0
                grand_total = total + tax - discount

                new_order = OrderModel(id,name, mobile_no, order_date, order, total, create_by, status, tax, tax_percent, discount, grand_total).__dict__
                ORDER.orders.append(new_order)
                ORDER.save_order()
                print('order save successful')
                return new_order['id']
        
            else:
                print('No items in your order to save')
    except Exception as error:
        print(error)

def review_order(order):
    try:
        if(order):
            total = 0
            print('{:<20}{:<10}{:<10}{:<10}'.format('NAME', 'RATE', 'QTY', 'TOTAL'))
            print('-'*50)
            for item in order:
                sum = item['sale_price'] * item['quantity']
                total += sum
                print('{:<20}{:<10}{:<10}{:<10}'.format(item['name'], item['sale_price'], item['quantity'], sum))

            print(f'TOTAL : {total}')
        else:
            print('items not available to review') 
    except Exception as error:
        print(error)

def payment_proceed(order_id):
    try:

        if(check_order(order_id)):
            ORDER = Order()
            for order in ORDER.orders:
                if(order['id'] == order_id):
                    if(order['status'] == 'process'):
                        is_paid = pay(order_id)
                        if(is_paid == 'success'):
                            order['status'] = 'paid'
                            ORDER.save_order()
                            print('payment successful')
                    else:
                        print('Order not in process or paid')
        else:
            print('order not found')
    except Exception as error:
        print(error)

def update_order():
    try:
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
                        order['tax'] += round((total / 100 * Default().tax_percent), 2)
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
    except Exception as error:
        print(error)