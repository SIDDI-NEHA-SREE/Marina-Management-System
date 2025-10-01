from src.dao.base_dao import BaseDAO
from src.models.staff import Staff

class StaffService:
    def __init__(self):
        self.dao = BaseDAO("mmsstaff", "staff_id")

    def add_staff(self, staff: Staff):
        return self.dao.insert(staff.to_dict())

    def list_staff(self):
        return self.dao.select().data

    def update_staff(self, staff_id, updated_data):
        return self.dao.update(staff_id, updated_data)

    def delete_staff(self, staff_id):
        return self.dao.delete(staff_id)
