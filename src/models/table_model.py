class TableModel:
    def __init__(self, id, seating_capacity):
        self.id = id
        self.seating_capacity = seating_capacity

    def __str__(self):
        return {
            "id":{self.id},
            "seating_capacity":{self.seating_capacity}
        }