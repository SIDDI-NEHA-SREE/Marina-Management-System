import os
import streamlit as st
from supabase import create_client

class BaseDAO:
    def __init__(self, table: str):
        # Streamlit Cloud secrets first, fallback to local .env
        supabase_url = st.secrets.get("SUPABASE_URL", os.getenv("SUPABASE_URL"))
        supabase_key = st.secrets.get("SUPABASE_KEY", os.getenv("SUPABASE_KEY"))

        if not supabase_url or not supabase_key:
            raise RuntimeError("Missing SUPABASE_URL or SUPABASE_KEY")

        self.client = create_client(supabase_url, supabase_key)
        self.table = table

    def insert(self, data: dict):
        return self.client.table(self.table).insert(data).execute()

    def select(self, filters: dict = None):
        query = self.client.table(self.table).select("*")
        if filters:
            for key, value in filters.items():
                query = query.eq(key, value)
        return query.execute()

    def update(self, data: dict, filters: dict):
        query = self.client.table(self.table).update(data)
        for key, value in filters.items():
            query = query.eq(key, value)
        return query.execute()

    def delete(self, filters: dict):
        query = self.client.table(self.table).delete()
        for key, value in filters.items():
            query = query.eq(key, value)
        return query.execute()
