from src.services.base_service import BaseService
from src.models.vessel import Vessel

class VesselsService(BaseService):
    def __init__(self):
        super().__init__("mmsvessels")

    def create_vessel(self, vessel: Vessel):
        return self.insert(vessel.to_dict())

    def update_vessel(self, vessel_id, data: dict):
        return self.update(vessel_id, data, "vessel_id")

    def delete_vessel(self, vessel_id):
        return self.delete(vessel_id, "vessel_id")

    def list_vessels(self):
        return self.select_all()

