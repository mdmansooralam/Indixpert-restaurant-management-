





from src.controllers.order_controller.order_report import get_order_by_date, get_order_by_day
from src.utility.validation import validate_id
from src.controllers.order_controller.order import payment_proceed
from src.controllers.order_controller.order_report import view_invoice, get_order_details

def display_order_by_date():
    date = input('Order Date : ')
    get_order_by_date(date)

def display_order_by_days():
    days = int(input('enter the days : '))
    get_order_by_day(days)

def pay_bill():
    id = validate_id(input('Order Id : '))
    if(not id):
        print('you enter a wrong id please try again : ')
        return
    payment_proceed(id)

def invoice():
    order_id = validate_id(input('Order Id : '))
    if(not order_id):
        print('invalid order id')
        return
    view_invoice(order_id)

def view_order_details():
    try:
        order_id = validate_id(input('Order Id : '))
        if(not order_id):
            print('invalid order id')
            return
        get_order_details(order_id)
    
    except Exception as error:
        print(error)

