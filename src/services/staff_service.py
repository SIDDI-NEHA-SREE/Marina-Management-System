'''from src.dao.staff_dao import StaffDAO

class StaffService:
    def __init__(self):
        self.dao = StaffDAO()

    def add_staff_member(self, data: dict):
        if "role" not in data:
            raise ValueError("Staff member must have a role.")
        return self.dao.add_staff(data)

    def get_staff_info(self, staff_id: int):
        result = self.dao.get_staff(staff_id)
        if not result.data:
            raise ValueError("Staff not found")
        return result.data[0]

    def update_staff_info(self, staff_id: int, updates: dict):
        return self.dao.update_staff(staff_id, updates)

    def remove_staff(self, staff_id: int):
        return self.dao.delete_staff(staff_id)
'''
# src/services/staff_service.py
from src.dao.staff_dao import StaffDAO

class StaffService:
    def __init__(self):
        self.dao = StaffDAO()

    def get_all_staff(self):
        return self.dao.get_all_staff()

    def add_staff(self, name, role):
        return self.dao.add_staff(name, role)
