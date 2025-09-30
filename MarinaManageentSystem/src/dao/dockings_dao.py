from src.dao.base_dao import BaseDAO

class DockingsDAO(BaseDAO):
    def __init__(self):
        super().__init__("mmsdockings")
