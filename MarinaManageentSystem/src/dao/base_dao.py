from src.utils.supabase_client import supabase

class BaseDAO:
    def __init__(self, table: str):
        self.client = supabase
        self.table = table

    def insert(self, data: dict):
        try:
            res = self.client.table(self.table).insert(data).execute()
            return res.data
        except Exception as e:
            print("Insert error:", e)
            return None

    def update(self, record_id: int, data: dict, id_field="id"):
        try:
            res = (
                self.client.table(self.table)
                .update(data)
                .eq(id_field, record_id)
                .execute()
            )
            return res.data
        except Exception as e:
            print("Update error:", e)
            return None

    def delete(self, record_id: int, id_field="id"):
        try:
            res = self.client.table(self.table).delete().eq(id_field, record_id).execute()
            return res.data
        except Exception as e:
            print("Delete error:", e)
            return None

    def get_all(self):
        try:
            res = self.client.table(self.table).select("*").execute()
            return res.data
        except Exception as e:
            print("Get all error:", e)
            return []
