'''from src.dao.payment_dao import PaymentDAO

class PaymentService:
    def __init__(self):
        self.dao = PaymentDAO()

    def record_payment(self, data: dict):
        if data.get("amount", 0) <= 0:
            raise ValueError("Payment amount must be positive.")
        return self.dao.add_payment(data)

    def get_payment_info(self, payment_id: int):
        result = self.dao.get_payment(payment_id)
        if not result.data:
            raise ValueError("Payment not found")
        return result.data[0]

    def update_payment(self, payment_id: int, updates: dict):
        return self.dao.update_payment(payment_id, updates)

    def remove_payment(self, payment_id: int):
        return self.dao.delete_payment(payment_id)
'''
# src/services/payment_service.py
from src.dao.payment_dao import PaymentDAO

class PaymentService:
    def __init__(self):
        self.dao = PaymentDAO()

    def get_all_payments(self):
        return self.dao.get_all_payments()

    def add_payment(self, owner_id, amount, status):
        return self.dao.add_payment(owner_id, amount, status)
