from config import get_supabase

class ViolationDAO:
    def __init__(self):
        self.supabase = get_supabase()

    def add_violation(self, data: dict):
        return self.supabase.table("mmsviolations").insert(data).execute()

    def get_violation(self, violation_id: int):
        return self.supabase.table("mmsviolations").select("*").eq("violation_id", violation_id).execute()

    def update_violation(self, violation_id: int, updates: dict):
        return self.supabase.table("mmsviolations").update(updates).eq("violation_id", violation_id).execute()

    def delete_violation(self, violation_id: int):
        return self.supabase.table("mmsviolations").delete().eq("violation_id", violation_id).execute()
