import plotly.express as px
import pandas as pd
from src.utils.supabase_client import supabase

class Dashboard:
    def __init__(self):
        self.client = supabase

    def vessel_type_distribution(self):
        res = self.client.table("mmsvessels").select("vessel_type").execute()
        if not res.data:
            return None
        df = pd.DataFrame(res.data)
        return px.pie(df, names="vessel_type", title="Vessel Type Distribution")

    def dock_occupancy(self):
        res = self.client.table("mmsdockings").select("dock_location, status").execute()
        if not res.data:
            return None
        df = pd.DataFrame(res.data)
        return px.histogram(df, x="dock_location", color="status", title="Dock Occupancy")

    def revenue_over_time(self):
        res = self.client.table("mmspayments").select("payment_date, amount").execute()
        if not res.data:
            return None
        df = pd.DataFrame(res.data)
        return px.line(df, x="payment_date", y="amount", title="Revenue Over Time")

    def violations_by_type(self):
        res = self.client.table("mmsviolations").select("violation_type").execute()
        if not res.data:
            return None
        df = pd.DataFrame(res.data)
        return px.histogram(df, x="violation_type", title="Violations by Type")
