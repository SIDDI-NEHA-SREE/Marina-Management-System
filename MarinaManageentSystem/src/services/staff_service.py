from src.dao.base_dao import BaseDAO

class StaffService:
    def __init__(self):
        self.dao = BaseDAO("mmsstaff")

    def add_staff(self, staff):
        return self.dao.insert(staff.to_dict())

    def list_staff(self):
        return self.dao.get_all()

    def update_staff(self, staff_id, data):
        return self.dao.update(staff_id, data, id_field="staff_id")

    def delete_staff(self, staff_id):
        return self.dao.delete(staff_id, id_field="staff_id")
