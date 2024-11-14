import uuid
from datetime import date
from src.utility.get_item import get_item
from src.utility.validation import validate_name, validate_int, validate_quantity, validate_mobile, validate_id, validate_blank, validate_size
from src.utility.error_message import ErrorMessage
from src.utility.get_order import get_order
from src.utility.check_order import check_order
from src.controllers.user_controller.user_state import UserState
from src.controllers.payment_gateway_controller.payment_gateway import pay
from src.controllers.reservation_controller.reservation import auto_reserve
from src.database.collections.order import Order
from src.database.collections.default import Default
from src.database.collections.item import Item
from src.models.order_model import OrderModel
from src.utility.get_input import get_input
from src.utility.log_error import LogError
from src.utility.colors import bcolors


def take_order():
    try:
        err_msg = ErrorMessage()
        order = []
        while True:
                choice = get_input(validate_blank, err_msg.enter_order_item, err_msg.invalid_item )
                if(not choice):
                    break
                        
                if choice == 'done':
                    break

                item = get_item(choice)
                if(item):
                    if(item['category'] == 'DRINK' or item['category'] == 'STARTER'):
                        quantity = get_input(validate_quantity, err_msg.enter_quantity, err_msg.invalid_quantity)
                        if(not quantity):
                            print(f'{bcolors.FAIL}{err_msg.invalid_quantity}')
                            break

                        if(item['quantity'] >= quantity):
                            item['quantity'] = quantity
                            order.append(item)
                            print(f'{bcolors.OKGREEN}{item['name']} {err_msg.added_to_order}')
                                        
                        else:
                            print(f'{bcolors.FAIL}Only {item['quantity']} {item['name']} available')
                    elif(item['category'] == 'MAIN COURSE'):
                        print(f'{bcolors.OKBLUE}F. Full')
                        print('H. Half')
                        print('Q. QUARTER')
                        size = get_input(validate_size, err_msg.choose_option, err_msg.invalid_option)
                        if(not size):
                            print(f'{bcolors.FAIL}{err_msg.invalid_option}')
                            continue

                        quantity = get_input(validate_quantity, err_msg.enter_quantity, err_msg.invalid_quantity)
                        if(not quantity):
                            print(f'{bcolors.FAIL}{err_msg.invalid_quantity}')
                            break

                        if(item['quantity'] >= quantity):
                            item['quantity'] = quantity
                            item['sale_price'] = item['sale_price'][size]
                            item['name'] += f' ({size.split("_")[0].upper()})'
                            order.append(item)
                            print(f'{bcolors.OKGREEN}{item['name']} {err_msg.added_to_order}')
                                        
                        else:
                            print(f'{bcolors.FAIL}Only {item['quantity']} {item['name']} available')
                        pass
                else:
                    print(err_msg.do_not_have_in_menu)

        return order
    except Exception as error:
        LogError().err.exception(error)
        print(error)

def finalize_order(order):
    try:
        ORDER = Order()
        ITEM = Item()
        err_msg = ErrorMessage()

        if(not order):
            raise Exception(err_msg.order_not_found)

        name = get_input(validate_name, err_msg.enter_customer_name, err_msg.invalid_name)
        if(not name):
            return
        
        mobile_no = get_input(validate_mobile, err_msg.enter_mobile_number, err_msg.invalid_mobile_number)
        if(not mobile_no):
            return
        
        print(err_msg.ask_for_table_booking)
        print(f'{bcolors.OKBLUE}1 YES')
        print('2 NO')
        option = get_input(validate_int, err_msg.choose_option, err_msg.invalid_option)
        if(not option):
            return
        
        if(option == 1):
            persons = get_input(validate_int, err_msg.number_of_person, err_msg.invalid_number_of_person)
            if(not persons):
                return
            
            res = auto_reserve(name, mobile_no, persons)
            if(not res):
                print(f'{bcolors.HEADER}{err_msg.continue_booking_without_table}')
                print(f'{bcolors.OKBLUE}1 YES')
                print('2 NO')
                action = get_input(validate_int, err_msg.choose_option, err_msg.invalid_option)
                if(not action):
                    return
                
                if(action == 2):
                    print('thank you')
                    return


        total = 0
        if order:
            for order_item in order:
                for item in ITEM.items:
                    if(item['id'] == order_item['id']):
                        item['quantity'] -= order_item['quantity']
                        #add total
                        total += order_item['sale_price'] * order_item['quantity']
                        ITEM.save_item()  

            id = str(uuid.uuid4())[:4].upper()
            order_date = date.today().strftime('%d-%m-%Y')
            create_by = UserState().get_state()['email']
            status = 'process'
            tax_percent = Default().tax_percent
            tax = round((total / 100 * tax_percent), 2)
            discount = 0
            grand_total = round(total + tax - discount)

            new_order = OrderModel(id,name, mobile_no, order_date, order, total, create_by, status, tax, tax_percent, discount, grand_total)._dict_
            ORDER.orders.append(new_order)
            ORDER.save_order()
            print(f'{bcolors.OKGREEN}{err_msg.order_saved}')
            return new_order['id']
        
        else:
            print(err_msg.no_item_in_order_list)
    except Exception as error:
        LogError().err.exception(error)
        print(f'{bcolors.FAIL}{error}')

def review_order(order):
    try:
        err_msg = ErrorMessage()
        if(order):
            total = 0
            fmt_str = '{:<30}{:<10}{:<10}{:<10}'
            print(f'{bcolors.HEADER}{fmt_str.format('NAME', 'RATE', 'QTY', 'TOTAL')}')
            print('-'*60)
            for item in order:
                sum = item['sale_price'] * item['quantity']
                total += sum
                print(f'{bcolors.OKBLUE}{fmt_str.format(item['name'], item['sale_price'], item['quantity'], sum)}')

            print(f'TOTAL : {total}')
        else:
            print(f'{bcolors.FAIL}{err_msg.item_not_found}') 
    except Exception as error:
        LogError().err.exception(error)
        print(f'{bcolors.FAIL}{error}')

def payment_proceed(order_id):
    try:
        err_msg = ErrorMessage()
        if(check_order(order_id)):
            ORDER = Order()
            for order in ORDER.orders:
                if(order['id'] == order_id):
                    if(order['status'] == 'process'):
                        is_paid = pay(order_id)
                        if(is_paid == 'success'):
                            order['status'] = 'paid'
                            ORDER.save_order()
                            print(f'{bcolors.OKGREEN}{err_msg.payment_success}')
                    elif(order['status'] == 'paid'):
                        print(f'{bcolors.FAIL}{err_msg.order_already_paid}')
                    else:
                        print(err_msg.order_not_found)
        else:
            print(err_msg.order_not_found)
    except Exception as error:
        LogError().err.exception(error)
        print(error)

def update_order():
    try:
        err_msg = ErrorMessage()
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
                            if(new_item['id'] == item['id']):
                                item['quantity'] -= new_item['quantity']
                                total += new_item['sale_price'] * new_item['quantity']
                                ITEM.save_item()
                
                for order in ORDER.orders:
                    if(order['id'] == id):
                        order['items'].extend(new_items)
                        order['total'] += total
                        order['tax'] += round((total / 100 * Default().tax_percent), 2)
                        order['grand_total'] = round(order['total'] + order['tax'] - order['discount'])
                        ORDER.save_order()
                        break
                
                print(f'{bcolors.OKBLUE}P. Pay')
                print('press any key to save')
                action = input(err_msg.choose_option).lower()

                if(action.lower() == 'p'):
                    payment_proceed(id)
                else:
                    print(err_msg.order_saved)
            else:
                print(f'{bcolors.FAIL}{err_msg.order_already_complete}')
        else:
            print(err_msg.invalid_id)
    except Exception as error:
        LogError().err.exception(error)
        print(error)