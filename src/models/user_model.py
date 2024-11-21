class UserModel:
    def __init__(
            self,
            id,
            name,
            email,
            password,
            date_of_birth,
            mobile_number,
            address,
            salary,
            date_of_joining,
            role,
            employment_type,
            shift_preferences,
            status,
            benefits,
            gender
    ):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.mobile_number = mobile_number
        self.address = address
        self.role = role
        self.salary = salary
        self.employment_type = employment_type
        self.date_of_joining = date_of_joining
        self.shift_preferences = shift_preferences
        self.status = status
        self.benefits = benefits
        self.password = password
        self.gender = gender


    def __str__(self):
        return {
            "id":{self.id},
            "name":{self.name},
            "date_of_birth":{self.date_of_birth},
            "email":{self.email},
            "mobile_number":{self.mobile_number},
            "address":{self.address},
            "role":{self.role},
            "salary":{self.salary},
            "employment_type":{self.employment_type},
            "date_of_joining":{self.date_of_joining},
            "shift_preferences":{self.shift_preferences},
            "status":{self.status},
            "benefits":{self.benefits},
            "password":{self.password},
            "gender":{self.gender}
        }