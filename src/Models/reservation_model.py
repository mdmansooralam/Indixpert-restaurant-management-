class ReservationModel:
    def __init__(self, id, table_id, date, time_slot, persons, name, status):
        self.id = id
        self.name = name
        self.table_id = table_id
        self.date = date
        self.time_slot = time_slot
        self.persons = persons
        self.status = status

    def __str__(self):
        return {
            "id" : {self.id},
            "name" : {self.name},
            "table_id" : {self.table_id},
            "date" : {self.date},
            "time_slot" : {self.time_slot},
            "persons" : {self.persons},
            'status':{self.status}
        }