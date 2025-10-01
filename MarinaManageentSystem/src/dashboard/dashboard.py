import plotly.express as px
import pandas as pd
from src.utils.supabase_client import supabase

class Dashboard:
    def __init__(self):
        self.client = supabase

    def vessel_type_distribution(self):
        try:
            res = self.client.table("mmsvessels").select("vessel_type").execute()
            data = res.data
            if not data:
                return None
            df = pd.DataFrame(data)
            return px.histogram(df, x="vessel_type", title="Vessel Type Distribution")
        except Exception as e:
            print("Dashboard error:", e)
            return None

    def dock_occupancy(self):
        try:
            res = self.client.table("mmsdockings").select("status").execute()
            data = res.data
            if not data:
                return None
            df = pd.DataFrame(data)
            return px.histogram(df, x="status", title="Dock Occupancy Status")
        except:
            return None

    def revenue_over_time(self):
        try:
            res = self.client.table("mmspayments").select("payment_date,amount").execute()
            data = res.data
            if not data:
                return None
            df = pd.DataFrame(data)
            df["payment_date"] = pd.to_datetime(df["payment_date"])
            return px.line(df, x="payment_date", y="amount", title="Revenue Over Time")
        except:
            return None

    def violations_by_type(self):
        try:
            res = self.client.table("mmsviolations").select("violation_type").execute()
            data = res.data
            if not data:
                return None
            df = pd.DataFrame(data)
            return px.histogram(df, x="violation_type", title="Violations by Type")
        except:
            return None
