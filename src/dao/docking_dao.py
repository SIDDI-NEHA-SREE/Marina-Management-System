'''from config import get_supabase

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
'''
# src/dao/docking_dao.py
from config import supabase

class DockingDAO:
    def __init__(self):
        self.client = supabase

    def get_all_dockings(self):
        resp = self.client.table("dockings").select("*").order("id", {"ascending": True}).execute()
        if getattr(resp, "error", None):
            raise Exception(resp.error)
        return resp.data or []

    def add_docking(self, vessel_id, dock_number, duration):
        payload = {"vessel_id": vessel_id, "dock_number": dock_number, "duration": duration}
        resp = self.client.table("dockings").insert(payload).execute()
        if getattr(resp, "error", None):
            raise Exception(resp.error)
        return (resp.data or [None])[0]
