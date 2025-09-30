from src.dao.base_dao import BaseDAO

class StaffDAO(BaseDAO):
    def __init__(self):
        super().__init__("mmsstaff")
