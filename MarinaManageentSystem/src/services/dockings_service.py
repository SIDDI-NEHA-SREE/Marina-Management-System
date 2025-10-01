from datetime import datetime
from src.dao.dockings_dao import DockingsDAO
from src.models.docking import Docking

class DockingsService:
    def __init__(self):
        self.dao = DockingsDAO()

    def dock_vessel(self, docking: Docking):
        docking.arrival_time = docking.arrival_time or datetime.utcnow()
        return self.dao.insert(docking.to_dict())

    def undock_vessel(self, docking_id: int, departure_time: datetime):
        # fetch docking record
        res = self.dao.select({"docking_id": docking_id})
        if not res.data:
            return {"error": "Docking not found"}

        row = res.data[0]
        arrival = datetime.fromisoformat(row["arrival_time"]) if row.get("arrival_time") else datetime.utcnow()
        stay = departure_time - arrival

        update_payload = {
            "departure_time": departure_time.isoformat(),
            "stay_duration": str(stay),
            "status": "vacated"
        }
        return self.dao.update(update_payload, {"docking_id": docking_id})

    def list_dockings(self):
        return self.dao.select().data
