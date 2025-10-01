from src.dao.base_dao import BaseDAO
from src.models.docking import Docking

class DockingsService:
    def __init__(self):
        self.dao = BaseDAO("mmsdockings", "docking_id")

    def dock_vessel(self, docking: Docking):
        return self.dao.insert(docking.to_dict())

    def list_dockings(self):
        return self.dao.select().data

    def update_docking(self, docking_id, updated_data):
        return self.dao.update(docking_id, updated_data)

    def delete_docking(self, docking_id):
        return self.dao.delete(docking_id)
