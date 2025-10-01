from datetime import datetime, timezone

class Payment:
    def __init__(
        self,
        vessel_id,
        amount,
        payment_type,
        tax_amount=0.0,
        payment_date=None,
        payment_id=None,
    ):
        self.payment_id = payment_id
        self.vessel_id = vessel_id
        self.amount = amount
        self.payment_type = payment_type
        self.tax_amount = tax_amount
        # use DB default if not provided
        self.payment_date = payment_date  

    def to_dict(self):
        data = {
            "vessel_id": self.vessel_id,
            "amount": self.amount,
            "payment_type": self.payment_type,
            "tax_amount": self.tax_amount,
        }
        if self.payment_date is not None:
            # if user gave a datetime → enforce UTC
            if isinstance(self.payment_date, datetime):
                data["payment_date"] = self.payment_date.astimezone(timezone.utc).isoformat()
            else:  
                data["payment_date"] = str(self.payment_date)  # if already date
        if self.payment_id is not None:
            data["payment_id"] = self.payment_id
        return data
