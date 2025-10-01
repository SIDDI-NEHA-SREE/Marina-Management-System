class Staff:
    def __init__(self, name, role, contact_info):
        self.name = name
        self.role = role
        self.contact_info = contact_info

    def to_dict(self):
        return {
            "name": self.name,
            "role": self.role,
            "contact_info": self.contact_info,
        }
