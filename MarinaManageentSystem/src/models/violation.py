from datetime import date

class Violation:
    def __init__(self, vessel_id, violation_type, details=None,
                 date_reported=None, resolved_status="pending", violation_id=None):
        self.violation_id = violation_id
        self.vessel_id = vessel_id
        self.violation_type = violation_type
        self.details = details
        self.date_reported = date_reported or date.today()
        self.resolved_status = resolved_status

    def to_dict(self):
        data = {
            "vessel_id": self.vessel_id,
            "violation_type": self.violation_type,
            "details": self.details,
            "date_reported": str(self.date_reported),
            "resolved_status": self.resolved_status,
        }
        if self.violation_id is not None:
            data["violation_id"] = self.violation_id
        return data
