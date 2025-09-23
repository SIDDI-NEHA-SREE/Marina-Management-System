from config import get_supabase

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
