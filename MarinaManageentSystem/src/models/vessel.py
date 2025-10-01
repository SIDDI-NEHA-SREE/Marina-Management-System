class Vessel:
    def __init__(self, vessel_name, vessel_type, capacity, owner_id, registration_number, vessel_id=None):
        self.vessel_id = vessel_id
        self.vessel_name = vessel_name
        self.vessel_type = vessel_type
        self.capacity = capacity
        self.owner_id = owner_id
        self.registration_number = registration_number

    def to_dict(self):
        return {
            "vessel_name": self.vessel_name,
            "vessel_type": self.vessel_type,
            "capacity": self.capacity,
            "owner_id": self.owner_id,
            "registration_number": self.registration_number,
        }
