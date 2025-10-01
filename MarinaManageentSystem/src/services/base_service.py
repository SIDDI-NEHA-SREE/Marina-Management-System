import streamlit as st
from supabase import create_client

class BaseService:
    def __init__(self, table_name: str):
        self.table = table_name
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        self.client = create_client(url, key)

    def insert(self, data: dict):
        return self.client.table(self.table).insert(data).execute()

    def update(self, record_id: int, data: dict, id_field="id"):
        return self.client.table(self.table).update(data).eq(id_field, record_id).execute()

    def delete(self, record_id: int, id_field="id"):
        return self.client.table(self.table).delete().eq(id_field, record_id).execute()

    def select_all(self):
        return self.client.table(self.table).select("*").execute().data
