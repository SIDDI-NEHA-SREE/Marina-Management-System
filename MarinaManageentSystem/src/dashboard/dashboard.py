import streamlit as st
import plotly.express as px
from supabase import create_client
import pandas as pd


class Dashboard:
    def __init__(self):
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        self.client = create_client(url, key)

    def vessel_type_distribution(self):
        try:
            res = self.client.table("mmsvessels").select("vessel_type").execute()
            df = pd.DataFrame(res.data)
            if df.empty:
                return None
            return px.histogram(df, x="vessel_type", title="Vessel Type Distribution")
        except Exception as e:
            st.error(f"Error: {e}")
            return None

    def dock_occupancy(self):
        try:
            res = self.client.table("mmsdockings").select("status").execute()
            df = pd.DataFrame(res.data)
            if df.empty:
                return None
            return px.histogram(df, x="status", title="Dock Occupancy")
        except Exception as e:
            st.error(f"Error: {e}")
            return None

    def revenue_over_time(self):
        try:
            res = self.client.table("mmspayments").select("payment_date, amount").execute()
            df = pd.DataFrame(res.data)
            if df.empty:
                return None
            df["payment_date"] = pd.to_datetime(df["payment_date"])
            return px.line(df, x="payment_date", y="amount", title="Revenue Over Time")
        except Exception as e:
            st.error(f"Error: {e}")
            return None

    def violations_by_type(self):
        try:
            res = self.client.table("mmsviolations").select("violation_type").execute()
            df = pd.DataFrame(res.data)
            if df.empty:
                return None
            return px.histogram(df, x="violation_type", title="Violations by Type")
        except Exception as e:
            st.error(f"Error: {e}")
            return None

