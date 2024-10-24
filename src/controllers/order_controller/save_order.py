from datetime import date
import uuid

from src.models.order_model import OrderModel
from src.manage_files.item import Item
from src.controllers.user_controller.user_state import UserState
from src.manage_files.order import Order
from src.utility.validation import validate_mobile


def finalize_order(order):
    ORDER = Order()
    ITEM = Item()

    mobile_no = validate_mobile(input('Customer Mobile Number : '))

    if(not mobile_no):
        print('please enter a valid mobile number')

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
            order_date = str(date.today())
            create_by = UserState().get_state()['email']
            status = 'process'

            new_order = OrderModel(id, mobile_no, order_date, order, total, create_by, status).__dict__
            ORDER.orders.append(new_order)
            ORDER.save_order()
            print('order finalize successful')
    
        else:
            print('No items in your order to finalize')