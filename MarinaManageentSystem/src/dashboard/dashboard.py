import plotly.express as px
import pandas as pd
from src.utils.supabase_client import supabase

class Dashboard:
    def __init__(self):
        self.client = supabase

    def vessel_type_distribution(self):
        """Pie chart of vessels by type"""
        res = self.client.table("MMSVessels").select("vessel_type").execute()
        if not res.data:
            return None
        df = pd.DataFrame(res.data)
        fig = px.pie(df, names="vessel_type", title="Vessel Type Distribution")
        return fig

    def dock_occupancy(self):
        """Bar chart of dock occupancy"""
        res = self.client.table("MMSDockings").select("dock_location, status").execute()
        if not res.data:
            return None
        df = pd.DataFrame(res.data)
        fig = px.histogram(df, x="dock_location", color="status", title="Dock Occupancy")
        return fig

    def revenue_over_time(self):
        """Line chart of revenue"""
        res = self.client.table("MMSPayments").select("payment_date, amount").execute()
        if not res.data:
            return None
        df = pd.DataFrame(res.data)
        fig = px.line(df, x="payment_date", y="amount", title="Revenue Over Time")
        return fig

    def violations_by_type(self):
        """Bar chart of violations"""
        res = self.client.table("MMSViolations").select("violation_type").execute()
        if not res.data:
            return None
        df = pd.DataFrame(res.data)
        fig = px.histogram(df, x="violation_type", title="Violations by Type")
        return fig
