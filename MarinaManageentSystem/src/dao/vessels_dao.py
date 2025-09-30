from src.dao.base_dao import BaseDAO

class VesselsDAO(BaseDAO):
    def __init__(self):
        super().__init__("mmsvessels")
