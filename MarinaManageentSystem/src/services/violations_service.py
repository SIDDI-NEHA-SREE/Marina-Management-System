from src.dao.violations_dao import ViolationsDAO
from src.models.violation import Violation

class ViolationsService:
    def __init__(self):
        self.dao = ViolationsDAO()

    def report_violation(self, violation: Violation):
        return self.dao.insert(violation.to_dict())

    def list_violations(self):
        return self.dao.select().data
