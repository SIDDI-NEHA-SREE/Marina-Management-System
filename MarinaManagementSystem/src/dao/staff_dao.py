from config import get_supabase

class StaffDAO:
    def __init__(self):
        self.supabase = get_supabase()

    def add_staff(self, data: dict):
        return self.supabase.table("mmsstaff").insert(data).execute()

    def get_staff(self, staff_id: int):
        return self.supabase.table("mmsstaff").select("*").eq("staff_id", staff_id).execute()

    def update_staff(self, staff_id: int, updates: dict):
        return self.supabase.table("mmsstaff").update(updates).eq("staff_id", staff_id).execute()

    def delete_staff(self, staff_id: int):
        return self.supabase.table("mmsstaff").delete().eq("staff_id", staff_id).execute()
