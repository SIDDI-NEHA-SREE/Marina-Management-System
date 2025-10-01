from datetime import date

class Violation:
    def __init__(self, vessel_id, violation_type, details):
        self.vessel_id = vessel_id
        self.violation_type = violation_type
        self.details = details
        self.date_reported = date.today()

    def to_dict(self):
        return {
            "vessel_id": self.vessel_id,
            "violation_type": self.violation_type,
            "details": self.details,
            "date_reported": str(self.date_reported),
        }
