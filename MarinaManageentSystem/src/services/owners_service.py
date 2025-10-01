from src.utils.supabase_client import supabase
from src.models.owner import Owner

class OwnersService:
    def __init__(self):
        self.client = supabase
        self.table = "mmsowners"

    def create_owner(self, owner: Owner):
        """Insert a new owner into the database"""
        res = self.client.table(self.table).insert(owner.to_dict()).execute()
        return res.data

    def list_owners(self):
        """Fetch all owners"""
        res = self.client.table(self.table).select("*").execute()
        return res.data

    def update_owner(self, owner_id: int, updated_data: dict):
        """Update owner details"""
        res = self.client.table(self.table).update(updated_data).eq("owner_id", owner_id).execute()
        return res.data

    def delete_owner(self, owner_id: int):
        """Delete owner by ID"""
        res = self.client.table(self.table).delete().eq("owner_id", owner_id).execute()
        return res.data

