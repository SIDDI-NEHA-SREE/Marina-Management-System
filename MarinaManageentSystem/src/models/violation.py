from datetime import datetime, timezone

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
        # always provide, since NOT NULL
        self.date_reported = date_reported or datetime.now(timezone.utc)
        self.resolved_status = resolved_status

    def to_dict(self):
        data = {
            "vessel_id": self.vessel_id,
            "violation_type": self.violation_type,
            "details": self.details,
            "date_reported": self.date_reported.isoformat(),
            "resolved_status": self.resolved_status,
        }
        if self.violation_id is not None:
            data["violation_id"] = self.violation_id
        return data
