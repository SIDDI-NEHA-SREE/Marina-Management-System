from datetime import datetime

class Docking:
    def __init__(self, vessel_id, dock_location, dock_capacity):
        self.vessel_id = vessel_id
        self.dock_location = dock_location
        self.dock_capacity = dock_capacity
        self.arrival_time = datetime.utcnow()

    def to_dict(self):
        return {
            "vessel_id": self.vessel_id,
            "dock_location": self.dock_location,
            "dock_capacity": self.dock_capacity,
            "arrival_time": self.arrival_time.isoformat(),
        }
