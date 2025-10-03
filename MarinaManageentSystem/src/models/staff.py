
class Staff:
    def __init__(self, name, role, contact_info, password, staff_id=None):
        self.staff_id = staff_id
        self.name = name
        self.role = role
        self.contact_info = contact_info
        self.password = password

    def to_dict(self):
        return {
            "staff_id": self.staff_id,
            "name": self.name,
            "role": self.role,
            "contact_info": self.contact_info,
            "password": self.password
        }

