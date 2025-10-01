class Staff:
    def __init__(self, name, role="", contact_info="", staff_id=None):
        self.staff_id = staff_id
        self.name = name
        self.role = role
        self.contact_info = contact_info

    def to_dict(self):
        data = {
            "name": self.name,
            "role": self.role,
            "contact_info": self.contact_info,
        }
        if self.staff_id is not None:
            data["staff_id"] = self.staff_id
        return data
