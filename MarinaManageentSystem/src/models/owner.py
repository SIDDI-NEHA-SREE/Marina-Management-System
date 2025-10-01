class Owner:
    def __init__(self, name, address, phone, email, owner_id=None):
        self.owner_id = owner_id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
        }
