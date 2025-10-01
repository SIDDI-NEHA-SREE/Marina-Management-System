from src.dao.base_dao import BaseDAO
from src.models.payment import Payment

class PaymentsService:
    def __init__(self):
        self.dao = BaseDAO("mmspayments", "payment_id")

    def record_payment(self, payment: Payment):
        return self.dao.insert(payment.to_dict())

    def list_payments(self):
        return self.dao.select().data
