from src.dao.base_dao import BaseDAO
from src.models.violation import Violation

class ViolationsService:
    def __init__(self):
        self.dao = BaseDAO("mmsviolations", "violation_id")

    def report_violation(self, violation: Violation):
        return self.dao.insert(violation.to_dict())

    def list_violations(self):
        return self.dao.select().data
