from src.dao.base_dao import BaseDAO

class VesselsService:
    def __init__(self):
        self.dao = BaseDAO("mmsvessels")

    def create_vessel(self, vessel):
        return self.dao.insert(vessel.to_dict())

    def list_vessels(self):
        return self.dao.get_all()

    def update_vessel(self, vessel_id, data):
        return self.dao.update(vessel_id, data, id_field="vessel_id")

    def delete_vessel(self, vessel_id):
        return self.dao.delete(vessel_id, id_field="vessel_id")
