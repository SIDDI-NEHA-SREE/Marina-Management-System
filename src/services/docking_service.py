'''from src.dao.docking_dao import DockingDAO

class DockingService:
    def __init__(self):
        self.dao = DockingDAO()

    def record_docking(self, data: dict):
        if "arrival_time" not in data:
            raise ValueError("Arrival time is required.")
        return self.dao.add_docking(data)

    def get_docking_info(self, docking_id: int):
        result = self.dao.get_docking(docking_id)
        if not result.data:
            raise ValueError("Docking not found")
        return result.data[0]

    def update_docking(self, docking_id: int, updates: dict):
        return self.dao.update_docking(docking_id, updates)

    def remove_docking(self, docking_id: int):
        return self.dao.delete_docking(docking_id)
'''
# src/services/docking_service.py
from src.dao.docking_dao import DockingDAO

class DockingService:
    def __init__(self):
        self.dao = DockingDAO()

    def get_all_dockings(self):
        return self.dao.get_all_dockings()

    def add_docking(self, vessel_id, dock_number, duration):
        return self.dao.add_docking(vessel_id, dock_number, duration)
