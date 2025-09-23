from src.dao.violation_dao import ViolationDAO

class ViolationService:
    def __init__(self):
        self.dao = ViolationDAO()

    def report_violation(self, data: dict):
        if "violation_type" not in data:
            raise ValueError("Violation must have a type.")
        return self.dao.add_violation(data)

    def get_violation_info(self, violation_id: int):
        result = self.dao.get_violation(violation_id)
        if not result.data:
            raise ValueError("Violation not found")
        return result.data[0]

    def update_violation(self, violation_id: int, updates: dict):
        return self.dao.update_violation(violation_id, updates)

    def resolve_violation(self, violation_id: int):
        return self.dao.update_violation(violation_id, {"resolved_status": "resolved"})

    def remove_violation(self, violation_id: int):
        return self.dao.delete_violation(violation_id)
