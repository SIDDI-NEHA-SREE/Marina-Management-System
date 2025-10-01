from src.services.base_service import BaseService
from src.models.payment import Payment

class PaymentsService(BaseService):
    def __init__(self):
        super().__init__("mmspayments")

    def record_payment(self, payment: Payment):
        return self.insert(payment.to_dict())

    def list_payments(self):
        return self.select_all()
