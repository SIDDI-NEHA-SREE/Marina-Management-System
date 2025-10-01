from datetime import date

class Violation:
    def __init__(self, vessel_id, violation_type, details, violation_id=None, date_reported=None, resolved_status="pending"):
        self.violation_id = violation_id
        self.vessel_id = vessel_id
        self.violation_type = violation_type
        self.details = details
        self.date_reported = date_reported or date.today()
        self.resolved_status = resolved_status

    def to_dict(self):
        return {
            "vessel_id": self.vessel_id,
            "violation_type": self.violation_type,
            "details": self.details,
            "date_reported": str(self.date_reported),
            "resolved_status": self.resolved_status,
        }
