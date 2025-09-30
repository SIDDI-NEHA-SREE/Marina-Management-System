'''# src/services/vessel_service.py
from src.dao.vessel_dao import VesselDAO

class VesselService:
    def __init__(self):
        self.dao = VesselDAO()

    def register_vessel(self, data: dict):
        if data.get("capacity", 0) <= 0:
            raise ValueError("Vessel capacity must be positive.")
        return self.dao.add_vessel(data)

    def get_vessel_info(self, vessel_id: int):
        result = self.dao.get_vessel(vessel_id)
        if not result.data:
            raise ValueError("Vessel not found")
        return result.data[0]

    def update_vessel_info(self, vessel_id: int, updates: dict):
        return self.dao.update_vessel(vessel_id, updates)

    def remove_vessel(self, vessel_id: int):
        return self.dao.delete_vessel(vessel_id)
'''
# src/services/vessel_service.py
from src.dao.vessel_dao import VesselDAO

class VesselService:
    def __init__(self):
        self.dao = VesselDAO()

    def get_all_vessels(self):
        return self.dao.get_all_vessels()

    def add_vessel(self, name, vessel_type, owner_id):
        return self.dao.add_vessel(name, vessel_type, owner_id)
