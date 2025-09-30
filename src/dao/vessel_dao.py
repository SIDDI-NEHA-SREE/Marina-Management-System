'''# src/dao/vessel_dao.py
from config import get_supabase

class VesselDAO:
    def __init__(self):
        self.supabase = get_supabase()

    def add_vessel(self, data: dict):
        return self.supabase.table("mmsvessels").insert(data).execute()

    def get_vessel(self, vessel_id: int):
        return self.supabase.table("mmsvessels").select("*").eq("vessel_id", vessel_id).execute()

    def update_vessel(self, vessel_id: int, updates: dict):
        return self.supabase.table("mmsvessels").update(updates).eq("vessel_id", vessel_id).execute()

    def delete_vessel(self, vessel_id: int):
        return self.supabase.table("mmsvessels").delete().eq("vessel_id", vessel_id).execute()
'''
# src/dao/vessel_dao.py
from config import supabase

class VesselDAO:
    def __init__(self):
        self.client = supabase

    def get_all_vessels(self):
        resp = self.client.table("vessels").select("*").order("id", {"ascending": True}).execute()
        if getattr(resp, "error", None):
            raise Exception(resp.error)
        return resp.data or []

    def add_vessel(self, name, vessel_type, owner_id):
        payload = {"name": name, "vessel_type": vessel_type, "owner_id": owner_id}
        resp = self.client.table("vessels").insert(payload).execute()
        if getattr(resp, "error", None):
            raise Exception(resp.error)
        return (resp.data or [None])[0]
