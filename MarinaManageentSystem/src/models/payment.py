from datetime import date

class Payment:
    def __init__(self, vessel_id, amount, payment_type, tax_amount=0.0, payment_id=None, payment_date=None):
        self.payment_id = payment_id
        self.vessel_id = vessel_id
        self.amount = amount
        self.payment_date = payment_date or date.today()
        self.payment_type = payment_type
        self.tax_amount = tax_amount

    def to_dict(self):
        return {
            "vessel_id": self.vessel_id,
            "amount": self.amount,
            "payment_date": str(self.payment_date),
            "payment_type": self.payment_type,
            "tax_amount": self.tax_amount,
        }
