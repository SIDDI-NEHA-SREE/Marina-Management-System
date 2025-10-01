from src.dao.vessels_dao import VesselsDAO
from src.models.vessel import Vessel

class VesselsService:
    def __init__(self):
        self.dao = VesselsDAO()

    def create_vessel(self, vessel: Vessel):
        return self.dao.insert(vessel.to_dict())

    def list_vessels(self):
        return self.dao.select().data
