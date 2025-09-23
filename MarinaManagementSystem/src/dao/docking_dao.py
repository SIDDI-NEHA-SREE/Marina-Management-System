from config import get_supabase

class DockingDAO:
    def __init__(self):
        self.supabase = get_supabase()

    def add_docking(self, data: dict):
        return self.supabase.table("mmsdockings").insert(data).execute()

    def get_docking(self, docking_id: int):
        return self.supabase.table("mmsdockings").select("*").eq("docking_id", docking_id).execute()

    def update_docking(self, docking_id: int, updates: dict):
        return self.supabase.table("mmsdockings").update(updates).eq("docking_id", docking_id).execute()

    def delete_docking(self, docking_id: int):
        return self.supabase.table("mmsdockings").delete().eq("docking_id", docking_id).execute()
