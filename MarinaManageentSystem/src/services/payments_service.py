from src.dao.base_dao import BaseDAO

class PaymentsService:
    def __init__(self):
        self.dao = BaseDAO("mmspayments")

    def record_payment(self, payment):
        return self.dao.insert(payment.to_dict())

    def list_payments(self):
        return self.dao.get_all()
