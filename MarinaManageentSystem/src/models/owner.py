class Owner:
    def __init__(self, name, address=None, phone=None, email=None, owner_id=None):
        self.owner_id = owner_id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def to_dict(self):
        data = {
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
        }
        if self.owner_id is not None:
            data["owner_id"] = self.owner_id
        return data
