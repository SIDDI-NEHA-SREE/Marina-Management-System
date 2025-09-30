'''from config import get_supabase

class PaymentDAO:
    def __init__(self):
        self.supabase = get_supabase()

    def add_payment(self, data: dict):
        return self.supabase.table("mmspayments").insert(data).execute()

    def get_payment(self, payment_id: int):
        return self.supabase.table("mmspayments").select("*").eq("payment_id", payment_id).execute()

    def update_payment(self, payment_id: int, updates: dict):
        return self.supabase.table("mmspayments").update(updates).eq("payment_id", payment_id).execute()

    def delete_payment(self, payment_id: int):
        return self.supabase.table("mmspayments").delete().eq("payment_id", payment_id).execute()
'''
# src/dao/payment_dao.py
from config import supabase

class PaymentDAO:
    def __init__(self):
        self.client = supabase

    def get_all_payments(self):
        resp = self.client.table("payments").select("*").order("id", {"ascending": True}).execute()
        if getattr(resp, "error", None):
            raise Exception(resp.error)
        return resp.data or []

    def add_payment(self, owner_id, amount, status):
        payload = {"owner_id": owner_id, "amount": amount, "status": status}
        resp = self.client.table("payments").insert(payload).execute()
        if getattr(resp, "error", None):
            raise Exception(resp.error)
        return (resp.data or [None])[0]
