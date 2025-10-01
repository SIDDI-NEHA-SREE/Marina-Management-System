from src.utils.supabase_client import supabase

class BaseDAO:
    def __init__(self, table_name, id_field=None):
        # Force lowercase table names to match Supabase/Postgres
        self.table = table_name.lower()
        self.client = supabase
        self.id_field = id_field or f"{self.table}_id"

    def insert(self, data: dict):
        return self.client.table(self.table).insert(data).execute()

    def select(self):
        return self.client.table(self.table).select("*").execute()

    def update(self, record_id, data: dict):
        return self.client.table(self.table).update(data).eq(self.id_field, record_id).execute()

    def delete(self, record_id):
        return self.client.table(self.table).delete().eq(self.id_field, record_id).execute()
