from src.dao.base_dao import BaseDAO

class ViolationsDAO(BaseDAO):
    def __init__(self):
        super().__init__("mmsviolations")
