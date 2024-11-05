from datetime import datetime




from src.database.collections.order import Order
from src.controllers.user_controller.user_state import UserState


def cancel_order(order_id):
    try:
        ORDER = Order()
        user_state = UserState().get_state()

        if(user_state['role'] == 'admin'):
            for order in ORDER.orders:
                if(order['id'] == order_id):
                    if(order['status'] == 'process'):
                        order['status'] = 'cancel'
                        ORDER.save_order()
                        print('Order cancel successful ')
                        return
                    elif(order['status']  == 'cancel'):
                        print('order already cancelled')
                        return
                    elif(order['status'] == 'paid'):
                        print('complete order can not be cancel')
                        return
            else:
                print('order not found')
    except Exception as error:
        print(error)

def get_order_by_date(date):
    try:
        orders = Order().orders

        order_found = False
        print('_'*60)
        print('{:<15}{:<15}{:<10}{:<10}{:<10}'.format('DATE', 'MOBILE NO', 'ORDER ID', 'TOTAL', 'STATUS'))
        print('_'*60)
        for order in orders:
            if(order['date'] == date):
                print(
                        '{:<15}{:<15}{:<10}{:<10}{:<10}'.format(
                            order['date'],
                            order['mobile_no'],
                            order['id'],
                            order['grand_total'],
                            order['status']
                        )
                    )
                order_found = True

        if(not order_found):
            print('order not found')
    except Exception as error:
        print(error)

def get_order_by_day(days):
    try:
        orders = Order().orders
        current_date = datetime.today()

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
            print('order record not available')
    except Exception as error:
        print(error)

def get_unpaid_order():
    try:
        orders = Order().orders
        unpaid_order_found = False
        print('_'*50)
        print('{:<15}{:<15}{:<10}{:<10}'.format('DATE', 'MOBILE NO', 'ORDER ID', 'TOTAL'))
        print('_'*50)
        for order in orders:
            if(order['status'] == 'process'):
                unpaid_order_found = True
                print(
                    '{:<15}{:<15}{:<10}{:<10}'.format(
                        order['date'],
                        order['mobile_no'],
                        order['id'],
                        order['grand_total'],
                        )
                    )
        if(not unpaid_order_found):
            print('no order in process')
    except Exception as error:
        print(error)

def view_invoice(order_id):
    try:
        orders = Order().orders

        for order in orders:
            if(order['id'] == order_id):
                if(order['status'] == 'process'):
                    print('Order still in process invoice not generated now')
                    return
                elif(order['status'] == 'cancel' or order['status'] == 'paid'):
                    print('__________________________INVOICE___________________________')
                    print('\n')
                    print('{:<15}{:<25}'.format('Name :', order['name']))
                    print('{:<15}{:<25}{:<10}{:<10}'.format('Mobile Number :', order['mobile_no'], 'Date :',order['date']))
                    print('{:<15}{:<25}{:<10}{:<10}'.format('Status :', order['status'], 'Order Id :', order['id']))

                    print('_'*65)
                    print('{:<5}{:<30}{:<10}{:<10}{:<10}'.format('S.No.', 'ITEM', 'RATE', 'QTY', 'TOTAL'))
                    print('_'*65)
                    item_count = 1
                    for item in order['items']:
                        print('{:<5}{:<30}{:<10}{:<10}{:<10}'.format(item_count, item['name'], item['sale_price'], item['quantity'], item['sale_price'] * item['quantity']))
                        item_count += 1
                    print('_'*65)
                    print('{:<35}{:<15}{:<10}'.format(' ', 'TOTAL', order['total']))
                    print('{:<35}{:<15}{:<10}'.format(' ', f'TAX({order['tax_percent']})', order['tax']))
                    print('\n')
                    print('{:<35}{:<15}{:<10}'.format(' ', 'GRAND TOTAL', order['grand_total']))
                    print('\n')
                    return
                else:
                    print('server error')
                    return
        else:
            print('invoice not found')
    except Exception as error:
        print(error)

def get_order_details(order_id):
    try:
        orders = Order().orders

        for order in orders:
            if(order['id'] == order_id):
                    print('__________________________ORDER DETAILS___________________________')
                    print('\n')
                    print('{:<15}{:<25}'.format('Name :', order['name']))
                    print('{:<15}{:<25}{:<10}{:<10}'.format('Mobile Number :', order['mobile_no'], 'Date :',order['date']))
                    print('{:<15}{:<25}{:<10}{:<10}'.format('Status :', order['status'], 'Order Id :', order['id']))

                    print('_'*60)
                    print('{:<5}{:<30}{:<10}{:<10}{:<10}'.format('S.No.', 'ITEM', 'RATE', 'QTY', 'TOTAL'))
                    print('_'*60)
                    item_count = 1
                    for item in order['items']:
                        print('{:<5}{:<30}{:<10}{:<10}{:<10}'.format(item_count, item['name'], item['sale_price'], item['quantity'], item['sale_price'] * item['quantity']))
                        item_count += 1
                    print('_'*60)
                    print('{:<35}{:<15}{:<10}'.format(' ', 'TOTAL', order['total']))
                    print('{:<35}{:<15}{:<10}'.format(' ', 'TAX', order['tax']))
                    print('\n')
                    print('{:<35}{:<15}{:<10}'.format(' ', 'GRAND TOTAL', order['grand_total']))
                    print('\n')

                    return
        else:
            print('order not found')
    except Exception as error:
        print(error)

def get_all_order():
    try:
        orders = Order().orders
        print('_'*60)
        print('{:<15}{:<15}{:<10}{:<10}{:<10}'.format('DATE', 'MOBILE NO', 'ORDER ID', 'TOTAL', 'STATUS'))
        print('_'*60)
        if(orders):
            for order in orders:
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
            print('order record not found')
    except Exception as error:
        print(error)