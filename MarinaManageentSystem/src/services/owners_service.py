from src.dao.owners_dao import OwnersDAO
from src.models.owner import Owner

class OwnersService:
    def __init__(self):
        self.dao = OwnersDAO()

    def create_owner(self, owner: Owner):
        return self.dao.insert(owner.to_dict())

    def list_owners(self):
        return self.dao.select().data
