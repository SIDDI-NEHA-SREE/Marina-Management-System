from config import get_supabase

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
