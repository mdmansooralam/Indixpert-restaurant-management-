class OrderModel:
    def __init__(self, id, mobile_no, date, items, total, create_by, status):
        self.id = id
        self.mobile_no = mobile_no
        self.date = date
        self.items = items
        self.total = total
        self.create_by = create_by
        self.status = status

    def __str__(self):
        return {
            "id":{self.id},
            "mobile_no":{self.mobile_no},
            "date":{self.date},
            "items":{self.items},
            "total":{self.total},
            "status":{self.status},
            "create_by":{self.create_by},
        }