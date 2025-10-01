from src.dao.payments_dao import PaymentsDAO
from src.models.payment import Payment

class PaymentsService:
    def __init__(self):
        self.dao = PaymentsDAO()

    def record_payment(self, payment: Payment):
        return self.dao.insert(payment.to_dict())

    def list_payments(self):
        return self.dao.select().data
