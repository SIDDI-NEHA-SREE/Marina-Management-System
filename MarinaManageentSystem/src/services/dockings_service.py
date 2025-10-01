from src.services.base_service import BaseService
from src.models.docking import Docking

class DockingsService(BaseService):
    def __init__(self):
        super().__init__("mmsdockings")

    def dock_vessel(self, docking: Docking):
        return self.insert(docking.to_dict())

    def update_docking(self, docking_id, data: dict):
        return self.update(docking_id, data, "docking_id")

    def delete_docking(self, docking_id):
        return self.delete(docking_id, "docking_id")

    def list_dockings(self):
        return self.select_all()
