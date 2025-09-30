from datetime import datetime

class Violation:
    def __init__(
        self,
        vessel_id,
        violation_type,
        details="",
        date_reported=None,
        resolved_status="pending",
        violation_id=None,
    ):
        self.violation_id = violation_id
        self.vessel_id = vessel_id
        self.violation_type = violation_type
        self.details = details
        self.date_reported = date_reported or datetime.utcnow()
        self.resolved_status = resolved_status

    def to_dict(self):
        return {
            "violation_id": self.violation_id,
            "vessel_id": self.vessel_id,
            "violation_type": self.violation_type,
            "details": self.details,
            "date_reported": self.date_reported.isoformat(),
            "resolved_status": self.resolved_status,
        }
