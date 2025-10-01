from src.dao.base_dao import BaseDAO

class OwnersService:
    def __init__(self):
        self.dao = BaseDAO("mmsowners")

    def create_owner(self, owner):
        return self.dao.insert(owner.to_dict())

    def list_owners(self):
        return self.dao.get_all()

    def update_owner(self, owner_id, data):
        return self.dao.update(owner_id, data, id_field="owner_id")

    def delete_owner(self, owner_id):
        return self.dao.delete(owner_id, id_field="owner_id")
