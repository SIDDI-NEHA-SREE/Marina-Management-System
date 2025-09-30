'''from config import get_supabase

class OwnerDAO:
    def __init__(self):
        self.supabase = get_supabase()

    def add_owner(self, data: dict):
        return self.supabase.table("mmsowners").insert(data).execute()

    def get_owner(self, owner_id: int):
        return self.supabase.table("mmsowners").select("*").eq("owner_id", owner_id).execute()

    def update_owner(self, owner_id: int, updates: dict):
        return self.supabase.table("mmsowners").update(updates).eq("owner_id", owner_id).execute()

    def delete_owner(self, owner_id: int):
        return self.supabase.table("mmsowners").delete().eq("owner_id", owner_id).execute()
'''
# src/dao/owner_dao.py
from config import supabase

class OwnerDAO:
    def __init__(self):
        # supabase client from config
        self.client = supabase

    def get_all_owners(self):
        """Return list of owner dicts (empty list if none)."""
        resp = self.client.table("owners").select("*").order("id", {"ascending": True}).execute()
        if getattr(resp, "error", None):
            # raise a readable exception
            raise Exception(resp.error)
        return resp.data or []

    def add_owner(self, name: str, email: str):
        payload = {"name": name, "email": email}
        resp = self.client.table("owners").insert(payload).execute()
        if getattr(resp, "error", None):
            raise Exception(resp.error)
        # resp.data is a list of inserted rows; return first
        return (resp.data or [None])[0]
