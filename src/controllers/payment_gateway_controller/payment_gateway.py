import uuid
from datetime import datetime


import traceback
from src.models.payment_model import PaymentModel
from src.database.collections.payments import Payment
from src.utility.get_order import get_order
from src.utility.validation import validate_price, validate_method
from src.utility.error_message import ErrorMessage
from src.utility.get_input import get_input
from src.utility.log_error import log
from src.utility.colors import bcolors


def pay(order_id):
    try:
        PAYMENT = Payment()
        order = get_order(order_id)
        err_msg = ErrorMessage()
        if(order):
            id = str(uuid.uuid4())[:10].upper()
            date = datetime.today().strftime('%d-%m-%Y')
            amount = order['grand_total']
            customer_contact = order['mobile_no']
            
            print('A. CASH')
            print('B. CARD')
            print('C. ONLINE')
            method = get_input(validate_method, err_msg.choose_option, err_msg.invalid_option)
            if(not method):
                raise Exception(err_msg.invalid_option)
                
            if(method == 'cash' or method == 'card' or method == 'online'):
                print(f'You have to pay {amount} Rupees')
                while True:
                    amt = get_input(validate_price, 'Enter Amount : ', 'Invalid Amount')
                    if(amt == amount):
                        status = 'success'
                        break
                    else:
                        print(f'{bcolors.FAIL}payment failed : you enter a wrong amount')
                        status = 'failed'

                new_payment = PaymentModel(id, date, amount, order_id, customer_contact, method, status).__dict__
                PAYMENT.payments.append(new_payment)
                PAYMENT.save_payment()
                if(status == 'failed'):
                    return 'failed'
                elif(status == 'success'):
                    return 'success'

        
        else:
            print(err_msg.order_not_found)
            return 'failed'
    except Exception as error:
        print(error)
        log(traceback.extract_tb(error.__traceback__)[0], error)
        return 'failed'