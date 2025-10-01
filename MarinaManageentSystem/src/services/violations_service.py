from src.dao.base_dao import BaseDAO

class ViolationsService:
    def __init__(self):
        self.dao = BaseDAO("mmsviolations")

    def report_violation(self, violation):
        return self.dao.insert(violation.to_dict())

    def list_violations(self):
        return self.dao.get_all()
