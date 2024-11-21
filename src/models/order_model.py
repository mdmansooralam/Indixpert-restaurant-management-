class OrderModel:
    def __init__(self, id, name, mobile_no, date, items, total, create_by, status, tax, tax_percent, discount, grand_total):
        self.id = id
        self.name = name
        self.mobile_no = mobile_no
        self.date = date
        self.items = items
        self.total = total
        self.create_by = create_by
        self.status = status
        self.tax = tax
        self.tax_percent = tax_percent
        self.discount = discount
        self.grand_total = grand_total

    def __str__(self):
        return {
            "id":{self.id},
            "name":{self.name},
            "mobile_no":{self.mobile_no},
            "date":{self.date},
            "items":{self.items},
            "total":{self.total},
            "status":{self.status},
            "create_by":{self.create_by},
            "tax_percent": {self.tax_percent},
            "tax":{self.tax},
            "discount":{self.discount},
            "grand_total":{self.grand_total},
        }