'''from src.dao.owner_dao import OwnerDAO


class OwnerService:
    def __init__(self):
        self.dao = OwnerDAO()

    def register_owner(self, data: dict):
        if "email" not in data:
            raise ValueError("Owner must have an email.")
        return self.dao.add_owner(data)

    def get_owner_info(self, owner_id: int):
        result = self.dao.get_owner(owner_id)
        if not result.data:
            raise ValueError("Owner not found")
        return result.data[0]

    def update_owner_info(self, owner_id: int, updates: dict):
        return self.dao.update_owner(owner_id, updates)

    def remove_owner(self, owner_id: int):
        return self.dao.delete_owner(owner_id)
'''
# src/services/owner_service.py
from src.dao.owner_dao import OwnerDAO

class OwnerService:
    def __init__(self):
        self.dao = OwnerDAO()

    def get_all_owners(self):
        return self.dao.get_all_owners()

    def add_owner(self, name, email):
        return self.dao.add_owner(name, email)
