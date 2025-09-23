# src/dao/vessel_dao.py
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
