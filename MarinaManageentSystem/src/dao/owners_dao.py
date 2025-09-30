from src.dao.base_dao import BaseDAO

class OwnersDAO(BaseDAO):
    def __init__(self):
        super().__init__("mmsowners")
