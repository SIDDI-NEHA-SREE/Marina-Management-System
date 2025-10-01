from src.dao.staff_dao import StaffDAO
from src.models.staff import Staff

class StaffService:
    def __init__(self):
        self.dao = StaffDAO()

    def add_staff(self, staff: Staff):
        return self.dao.insert(staff.to_dict())

    def list_staff(self):
        return self.dao.select().data
