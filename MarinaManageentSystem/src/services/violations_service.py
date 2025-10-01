from src.services.base_service import BaseService
from src.models.violation import Violation

class ViolationsService(BaseService):
    def __init__(self):
        super().__init__("mmsviolations")   # lowercase ✅

    def report_violation(self, violation: Violation):
        return self.insert(violation.to_dict())

    def list_violations(self):
        return self.select_all()
