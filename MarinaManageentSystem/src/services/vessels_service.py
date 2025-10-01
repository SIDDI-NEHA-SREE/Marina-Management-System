from src.services.base_service import BaseService
import pandas as pd

class ViolationsService(BaseService):
    def __init__(self):
        super().__init__("mmsviolations")

    def report_violation(self, violation):
        return self.insert(violation.to_dict())

    def list_violations(self):
        return self.fetch_all()

    def auto_check_violation(self, vessel_id, current_time, location):
        # Check if vessel is docked properly
        docking = self.client.table("mmsdockings").select("*").eq("vessel_id", vessel_id).order("arrival_time", desc=True).limit(1).execute()
        
        if not docking.data:
            # Unauthorized docking
            self.client.table("mmsviolations").insert({
                "vessel_id": vessel_id,
                "violation_type": "Unauthorized Docking",
                "details": f"Docked at {location} without record",
                "date_reported": str(current_time)
            }).execute()
            return

        # Overstay check (6 hours)
        allowed_hours = 6
        arrival = pd.to_datetime(docking.data[0]["arrival_time"])
        if (current_time - arrival).total_seconds() > allowed_hours * 3600:
            self.client.table("mmsviolations").insert({
                "vessel_id": vessel_id,
                "violation_type": "Overstay",
                "details": f"Stayed beyond {allowed_hours} hours",
                "date_reported": str(current_time)
            }).execute()
