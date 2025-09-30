'''from config import get_supabase

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
'''
# src/dao/staff_dao.py
from config import supabase

class StaffDAO:
    def __init__(self):
        self.client = supabase

    def get_all_staff(self):
        resp = self.client.table("staff").select("*").order("id", {"ascending": True}).execute()
        if getattr(resp, "error", None):
            raise Exception(resp.error)
        return resp.data or []

    def add_staff(self, name, role):
        payload = {"name": name, "role": role}
        resp = self.client.table("staff").insert(payload).execute()
        if getattr(resp, "error", None):
            raise Exception(resp.error)
        return (resp.data or [None])[0]
