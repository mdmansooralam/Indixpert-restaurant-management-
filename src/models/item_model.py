class ItemModel:
    def __init__(self, id, name, category, cost_price, sale_price, quantity, added_by):
        self.id = id
        self.name = name
        self.category = category
        self.cost_price = cost_price
        self.sale_price = sale_price
        self.quantity = quantity
        self.added_by = added_by

    def __str__(self):
        return {
            "id":{self.id},
            "name":{self.name},
            "category":{self.category},
            "cost_price":{self.cost_price},
            "sale_price":{self.sale_price},
            "quantity":{self.quantity},
            "added_by":{self.added_by},
        }
