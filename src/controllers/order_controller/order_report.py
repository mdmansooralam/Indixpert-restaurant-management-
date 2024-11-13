
from datetime import datetime
from src.database.collections.order import Order
from src.utility.validation import validate_id, validate_int, validate_date
from src.utility.error_message import ErrorMessage
from src.database.collections.user import User
from src.utility.log_error import LogError
from src.utility.get_input import get_input


def get_order_by_date():
    try:
        err_msg = ErrorMessage()
        orders = Order().orders
        date = get_input(validate_date, err_msg.enter_date, err_msg.invalid_date)
        if(not date):
            raise Exception(err_msg.invalid_date)
        order_found = False
        fmt_str = '{:<15}{:<15}{:<10}{:<10}{:<10}'
        print('_'*60)
        print(fmt_str.format('DATE', 'MOBILE NO', 'ORDER ID', 'TOTAL', 'STATUS'))
        print('_'*60)
        for order in orders:
            if(order['date'] == date):
                print(
                        fmt_str.format(
                            order['date'],
                            order['mobile_no'],
                            order['id'],
                            order['grand_total'],
                            order['status']
                        )
                    )
                order_found = True

        if(not order_found):
            print(err_msg.order_not_found)
    except Exception as error:
        LogError().err.exception(error)
        print(error)

def get_order_by_day():
    try:
        err_msg = ErrorMessage()
        orders = Order().orders
        current_date = datetime.today()
        days = get_input(validate_int, 'Enter days : ', 'Invalid days')
        if(not days):
            raise Exception('invalid days')
        
        if(orders):
            print('_'*60)
            print('{:<15}{:<15}{:<10}{:<10}{:<10}'.format('DATE', 'MOBILE NO', 'ORDER ID', 'TOTAL', 'STATUS'))
            print('_'*60)
            for order in orders:
                order_date = datetime.strptime(order['date'], '%d-%m-%Y')
                if((current_date - order_date).days <= days):
                    print(
                        '{:<15}{:<15}{:<10}{:<10}{:<10}'.format(
                            order['date'],
                            order['mobile_no'],
                            order['id'],
                            order['grand_total'],
                            order['status']
                        )
                    )
        else:
            print(err_msg.order_not_found)
    except Exception as error:
        LogError().err.exception(error)
        print(error)

def get_unpaid_order():
    try:
        err_msg = ErrorMessage()
        orders = Order().orders
        unpaid_order_found = False
        fmt_str = '{:<15}{:<15}{:<10}{:<10}'
        print('_'*50)
        print(fmt_str.format('DATE', 'MOBILE NO', 'ORDER ID', 'TOTAL'))
        print('_'*50)
        for order in orders:
            if(order['status'] == 'process'):
                unpaid_order_found = True
                print(
                    fmt_str.format(
                        order['date'],
                        order['mobile_no'],
                        order['id'],
                        order['grand_total'],
                        )
                    )
        if(not unpaid_order_found):
            print(err_msg.order_not_found)
    except Exception as error:
        LogError().err.exception(error)
        print(error)

def view_invoice(order_id):
    try:
        err_msg = ErrorMessage()
        orders = Order().orders

        fmt_2 = '{:<15}{:<25}'
        fmt_3 = '{:<40}{:<15}{:<10}'
        fmt_4 = '{:<15}{:<25}{:<10}{:<10}'
        fmt_5 = '{:<10}{:<30}{:<10}{:<10}{:<10}'
        for order in orders:
            if(order['id'] == order_id):
                if(order['status'] == 'process'):
                    print(err_msg.oder_in_process)
                    return
                elif(order['status'] == 'cancel' or order['status'] == 'paid'):
                    print('_____________________________INVOICE_____________________________')
                    print('\n')
                    print(fmt_2.format('Name :', order['name']))
                    print(fmt_4.format('Mobile Number :', order['mobile_no'], 'Date :',order['date']))
                    print(fmt_4.format('Status :', order['status'], 'Order Id :', order['id']))

                    print('_'*70)
                    print(fmt_5.format('S.No.', 'ITEM', 'RATE', 'QTY', 'TOTAL'))
                    print('_'*70)
                    item_count = 1
                    for item in order['items']:
                        print(fmt_5.format(item_count, item['name'], item['sale_price'], item['quantity'], item['sale_price'] * item['quantity']))
                        item_count += 1
                    print('_'*65)
                    print(fmt_3.format(' ', 'TOTAL', order['total']))
                    print(fmt_3.format(' ', f'TAX({order['tax_percent']}%)', order['tax']))
                    print('\n')
                    print(fmt_3.format(' ', 'GRAND TOTAL', order['grand_total']))
                    print('\n')
                    return
                else:
                    print('server error')
                    return
        else:
            print(err_msg.invoice_not_found)
    except Exception as error:
        LogError().err.exception(error)
        print(error)

def get_order_details():
    try:
        orders = Order().orders
        err_msg = ErrorMessage()
        order_id = get_input(validate_id, err_msg.enter_id, err_msg.invalid_id)
        if(not order_id):
            raise Exception(err_msg.invalid_id)
        
        fmt_2 = '{:<15}{:<25}'
        fmt_3 = '{:<40}{:<15}{:<10}'
        fmt_4 = '{:<15}{:<25}{:<10}{:<10}'
        fmt_5 = '{:<10}{:<30}{:<10}{:<10}{:<10}'
        for order in orders:
            if(order['id'] == order_id):
                    print('__________________________ORDER DETAILS___________________________')
                    print('\n')
                    print(fmt_2.format('Name :', order['name']))
                    print(fmt_4.format('Mobile Number :', order['mobile_no'], 'Date :',order['date']))
                    print(fmt_4.format('Status :', order['status'], 'Order Id :', order['id']))

                    print('_'*60)
                    print(fmt_5.format('S.No.', 'ITEM', 'RATE', 'QTY', 'TOTAL'))
                    print('_'*60)
                    item_count = 1
                    for item in order['items']:
                        print(fmt_5.format(item_count, item['name'], item['sale_price'], item['quantity'], item['sale_price'] * item['quantity']))
                        item_count += 1
                    print('_'*60)
                    print(fmt_3.format(' ', 'TOTAL', order['total']))
                    print(fmt_3.format(' ', f'TAX({order['tax_percent']}%)', order['tax']))
                    print('\n')
                    print(fmt_3.format(' ', 'GRAND TOTAL', order['grand_total']))
                    print('\n')

                    return
        else:
            print(err_msg.order_not_found)
    except Exception as error:
        LogError().err.exception(error)
        print(error)

def get_all_order():
    try:
        err_msg = ErrorMessage()
        orders = Order().orders
        fmt_str = '{:<15}{:<15}{:<10}{:<10}{:<10}'
        print('_'*60)
        print(fmt_str.format('DATE', 'MOBILE NO', 'ORDER ID', 'TOTAL', 'STATUS'))
        print('_'*60)
        if(orders):
            for order in orders:
                print(
                    fmt_str.format(
                        order['date'],
                        order['mobile_no'],
                        order['id'],
                        order['grand_total'],
                        order['status']
                    )
                )
        else:
            print(err_msg.order_not_found)
    except Exception as error:
        LogError().err.exception(error)
        print(error)

def get_order_staff_wise():
    try:
        users = User().users
        orders = Order().orders
        fmt_str = '{:<20}{:<20}{:<15}{:<15}'
        print(fmt_str.format('NAME', 'EMAIL', 'TOTAL ORDER', 'ORDER VALUE'))
        print('_'*70)
        for user in users:
            if(user['role'] == 'staff'):
                total_order_value = 0
                total_order = 0

                for order in orders:
                    if(order['create_by'] == user['email']):
                        total_order_value += order['grand_total']
                        total_order += 1
                        
                print(fmt_str.format(user['name'], user['email'], total_order, total_order_value))
    except Exception as error:
        print(error)
        LogError().err.exception(error)

def today_order():
    try:
        err_msg = ErrorMessage()
        orders = Order().orders
        # date = get_input(validate_date, err_msg.enter_date, err_msg.invalid_date)
        date = datetime.today().strftime("%d-%m-%Y")
        if(not date):
            raise Exception(err_msg.invalid_date)
        order_found = False
        fmt_str = '{:<15}{:<15}{:<10}{:<10}{:<10}'
        print('_'*60)
        print(fmt_str.format('DATE', 'MOBILE NO', 'ORDER ID', 'TOTAL', 'STATUS'))
        print('_'*60)
        for order in orders:
            if(order['date'] == date):
                print(
                        fmt_str.format(
                            order['date'],
                            order['mobile_no'],
                            order['id'],
                            order['grand_total'],
                            order['status']
                        )
                    )
                order_found = True

        if(not order_found):
            print(err_msg.order_not_found)
    except Exception as error:
        LogError().err.exception(error)
        print(error)