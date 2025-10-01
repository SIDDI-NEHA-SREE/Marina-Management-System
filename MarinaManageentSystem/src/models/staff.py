from datetime import datetime, date

class Payment:
    def __init__(self, vessel_id, amount, payment_type=None, tax_amount=0.0,
                 payment_date=None, payment_id=None):
        self.payment_id = payment_id
        self.vessel_id = vessel_id
        self.amount = amount
        self.payment_type = payment_type
        self.tax_amount = tax_amount
        # DB has DEFAULT now(), so keep optional
        self.payment_date = payment_date or date.today()

    def to_dict(self):
        data = {
            "vessel_id": self.vessel_id,
            "amount": self.amount,
            "payment_type": self.payment_type,
            "tax_amount": self.tax_amount,
            "payment_date": str(self.payment_date) if self.payment_date else None,
        }
        if self.payment_id is not None:
            data["payment_id"] = self.payment_id
        return data
