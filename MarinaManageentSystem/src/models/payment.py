from datetime import date

class Payment:
    def __init__(self, vessel_id, amount, payment_type, tax_amount=0.0):
        self.vessel_id = vessel_id
        self.amount = amount
        self.payment_type = payment_type
        self.tax_amount = tax_amount
        self.payment_date = date.today()

    def to_dict(self):
        return {
            "vessel_id": self.vessel_id,
            "amount": self.amount,
            "payment_type": self.payment_type,
            "tax_amount": self.tax_amount,
            "payment_date": str(self.payment_date),
        }
