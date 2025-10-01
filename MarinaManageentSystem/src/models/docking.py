from datetime import datetime, timezone

class Docking:
    def __init__(self, vessel_id, dock_location, dock_capacity=1, status="available", arrival_time=None, departure_time=None, docking_id=None):
        self.docking_id = docking_id
        self.vessel_id = vessel_id
        self.dock_location = dock_location
        self.dock_capacity = dock_capacity
        self.status = status
        self.arrival_time = arrival_time or datetime.now(timezone.utc)
        self.departure_time = departure_time

    def to_dict(self):
        return {
            "vessel_id": self.vessel_id,
            "dock_location": self.dock_location,
            "dock_capacity": self.dock_capacity,
            "status": self.status,
            "arrival_time": self.arrival_time.isoformat(),
            "departure_time": self.departure_time.isoformat() if self.departure_time else None,
        }
