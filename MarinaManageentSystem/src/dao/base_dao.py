import os
import streamlit as st
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()


class BaseDAO:
    def __init__(self, table: str):
        supabase_url = st.secrets.get("SUPABASE_URL", os.getenv("SUPABASE_URL"))
        supabase_key = st.secrets.get("SUPABASE_KEY", os.getenv("SUPABASE_KEY"))

        if not supabase_url or not supabase_key:
            raise RuntimeError("Missing SUPABASE_URL or SUPABASE_KEY")

        self.client = create_client(supabase_url, supabase_key)
        self.table = table

    # ---------- CRUD METHODS ----------

    def insert(self, data: dict):
        res = self.client.table(self.table).insert(data).execute()
        return res.data  # ✅ always return list of rows

    def fetch_all(self):
        res = self.client.table(self.table).select("*").execute()
        return res.data or []  # ✅ return list (empty if none)

    def fetch_by_id(self, record_id: int, id_column: str = None):
        id_column = id_column or f"{self.table[:-1]}_id"  # e.g. mmsowners -> owner_id
        res = self.client.table(self.table).select("*").eq(id_column, record_id).execute()
        return res.data[0] if res.data else None

    def update(self, record_id: int, data: dict, id_column: str = None):
        id_column = id_column or f"{self.table[:-1]}_id"
        res = self.client.table(self.table).update(data).eq(id_column, record_id).execute()
        return res.data  # ✅ return updated row(s)

    def delete(self, record_id: int, id_column: str = None):
        id_column = id_column or f"{self.table[:-1]}_id"
        res = self.client.table(self.table).delete().eq(id_column, record_id).execute()
        return res.data  # ✅ return deleted row(s)
