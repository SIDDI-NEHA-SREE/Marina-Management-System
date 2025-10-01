from src.dao.base_dao import BaseDAO

class DockingsService:
    def __init__(self):
        self.dao = BaseDAO("mmsdockings")

    def dock_vessel(self, docking):
        return self.dao.insert(docking.to_dict())

    def list_dockings(self):
        return self.dao.get_all()

    def update_docking(self, docking_id, data):
        return self.dao.update(docking_id, data, id_field="docking_id")

    def delete_docking(self, docking_id):
        return self.dao.delete(docking_id, id_field="docking_id")
