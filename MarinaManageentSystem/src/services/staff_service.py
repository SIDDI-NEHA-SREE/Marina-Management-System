from src.services.base_service import BaseService
from src.models.staff import Staff

class StaffService(BaseService):
    def __init__(self):
        super().__init__("mmsstaff")

    def add_staff(self, staff: Staff):
        return self.insert(staff.to_dict())

    def update_staff(self, staff_id, data: dict):
        return self.update(staff_id, data, "staff_id")

    def delete_staff(self, staff_id):
        return self.delete(staff_id, "staff_id")

    def list_staff(self):
        return self.select_all()
