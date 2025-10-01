from src.dao.base_dao import BaseDAO

class PaymentsDAO(BaseDAO):
    def __init__(self):
        super().__init__("mmspayments")
