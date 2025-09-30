'''from config import get_supabase

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
'''
# src/dao/violation_dao.py
from config import supabase

class ViolationDAO:
    def __init__(self):
        self.client = supabase

    def get_all_violations(self):
        resp = self.client.table("violations").select("*").order("id", {"ascending": True}).execute()
        if getattr(resp, "error", None):
            raise Exception(resp.error)
        return resp.data or []

    def add_violation(self, vessel_id, description, fine):
        payload = {"vessel_id": vessel_id, "description": description, "fine": fine}
        resp = self.client.table("violations").insert(payload).execute()
        if getattr(resp, "error", None):
            raise Exception(resp.error)
        return (resp.data or [None])[0]
