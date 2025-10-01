from src.services.base_service import BaseService
from src.models.owner import Owner

class OwnersService(BaseService):
    def __init__(self):
        super().__init__("mmsowners")

    def create_owner(self, owner: Owner):
        return self.insert(owner.to_dict())

    def update_owner(self, owner_id, data: dict):
        return self.update(owner_id, data, "owner_id")

    def delete_owner(self, owner_id):
        return self.delete(owner_id, "owner_id")

    def list_owners(self):
        return self.select_all()
