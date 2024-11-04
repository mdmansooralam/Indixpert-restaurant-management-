from datetime import date
import uuid

from src.models.order_model import OrderModel
from src.database.collections.item import Item
from src.controllers.user_controller.user_state import UserState
from src.database.collections.order import Order
from src.utility.validation import validate_mobile, validate_name
from src.constant import TAX


def finalize_order(order):
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
            tax_percent = TAX
            tax = total / 100 * TAX
            discount = 0
            grand_total = total + tax - discount

            new_order = OrderModel(id,name, mobile_no, order_date, order, total, create_by, status, tax, tax_percent, discount, grand_total).__dict__
            ORDER.orders.append(new_order)
            ORDER.save_order()
            print('order save successful')
            return new_order['id']
    
        else:
            print('No items in your order to save')