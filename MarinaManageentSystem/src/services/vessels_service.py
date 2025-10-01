from src.dao.base_dao import BaseDAO
from src.models.vessel import Vessel

class VesselsService:
    def __init__(self):
        self.dao = BaseDAO("mmsvessels", "vessel_id")

    def create_vessel(self, vessel: Vessel):
        return self.dao.insert(vessel.to_dict())

    def list_vessels(self):
        return self.dao.select().data

    def update_vessel(self, vessel_id, updated_data):
        return self.dao.update(vessel_id, updated_data)

    def delete_vessel(self, vessel_id):
        return self.dao.delete(vessel_id)
