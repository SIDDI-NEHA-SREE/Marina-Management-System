import pandas as pd
import plotly.express as px
from src.dao.vessels_dao import VesselsDAO
from src.dao.dockings_dao import DockingsDAO
from src.dao.payments_dao import PaymentsDAO
from src.dao.violations_dao import ViolationsDAO

class Dashboard:
    def __init__(self):
        self.vessels_dao = VesselsDAO()
        self.dockings_dao = DockingsDAO()
        self.payments_dao = PaymentsDAO()
        self.violations_dao = ViolationsDAO()

    def vessel_type_distribution(self):
        res = self.vessels_dao.select()
        df = pd.DataFrame(res.data or [])
        if df.empty:
            return None
        fig = px.pie(df, names="vessel_type", title="Vessels by Type")
        return fig

    def dock_occupancy(self):
        res = self.dockings_dao.select()
        df = pd.DataFrame(res.data or [])
        if df.empty:
            return None
        agg = df.groupby("dock_location").size().reset_index(name="occupied")
        fig = px.bar(agg, x="dock_location", y="occupied", title="Dock Occupancy")
        return fig

    def revenue_over_time(self):
        res = self.payments_dao.select()
        df = pd.DataFrame(res.data or [])
        if df.empty:
            return None
        df["payment_date"] = pd.to_datetime(df["payment_date"])
        df_group = df.groupby("payment_date")["amount"].sum().reset_index()
        fig = px.line(df_group, x="payment_date", y="amount", title="Revenue Over Time")
        return fig

    def violations_by_type(self):
        res = self.violations_dao.select()
        df = pd.DataFrame(res.data or [])
        if df.empty:
            return None
        fig = px.histogram(df, x="violation_type", title="Violations by Type")
        return fig
