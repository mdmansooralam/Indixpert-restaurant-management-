import uuid
from datetime import datetime



from src.models.payment_model import PaymentModel
from src.database.collections.payments import Payment
from src.utility.get_order import get_order
from src.utility.validation import validate_price

def pay(order_id):
    PAYMENT = Payment()
    order = get_order(order_id)
    if(order):
        id = str(uuid.uuid4())[:10].upper()
        date = datetime.today().strftime('%d-%m-%Y')
        amount = order['grand_total']
        customer_contact = order['mobile_no']

        method = input('Method (cash / card / online) : ').lower()
        if(method == 'cash' or method == 'card' or method == 'online'):
            print(f'You have to pay {amount} Rupees')
            amt = validate_price(input('Enter Amount : '))
            if(amt == amount):
                status = 'success'
            else:
                print('payment failed : you enter a wrong amount')
                status = 'failed'

            new_payment = PaymentModel(id, date, amount, order_id, customer_contact, method, status).__dict__
            PAYMENT.payments.append(new_payment)
            PAYMENT.save_payment()
            if(status == 'failed'):
                return 'failed'
            elif(status == 'success'):
                return 'success'

        else:
            print('payment failed : You chose a wrong method')
            return 'failed'

    
    else:
        print('somthing went wrong')
        return 'failed'