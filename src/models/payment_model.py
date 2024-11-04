



class PaymentModel:
    def __init__(self, id, date, amount, order_id, customer_contact, method, status):
        self.id = id
        self.date = date
        self.amount = amount
        self.order_id = order_id
        self.customer_contact = customer_contact
        self.method = method
        self.status = status

    def __str__(self):
        return {
            "id":{self.id},
            "date":{self.date},
            "amount":{self.amount},
            "order_id":{self.order_id},
            "customer_contact":{self.customer_contact},
            "method":{self.method},
            "status":{self.status},
        }