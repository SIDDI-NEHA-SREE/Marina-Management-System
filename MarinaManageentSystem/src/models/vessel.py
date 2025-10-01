class Vessel:
    def __init__(
        self,
        vessel_name,
        vessel_type="",
        capacity=0,
        owner_id=None,
        registration_number="",
        cargo=None,
        documents=None,
        vessel_id=None,
    ):
        self.vessel_id = vessel_id
        self.vessel_name = vessel_name
        self.vessel_type = vessel_type
        self.capacity = capacity
        self.owner_id = owner_id
        self.registration_number = registration_number
        self.cargo = cargo or {}
        self.documents = documents or {}

    def to_dict(self):
        data = {
            "vessel_name": self.vessel_name,
            "vessel_type": self.vessel_type,
            "capacity": self.capacity,
            "owner_id": self.owner_id,
            "registration_number": self.registration_number,
            "cargo": self.cargo,
            "documents": self.documents,
        }
        if self.vessel_id is not None:
            data["vessel_id"] = self.vessel_id
        return data
