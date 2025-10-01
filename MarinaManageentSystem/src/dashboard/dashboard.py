import pandas as pd
import plotly.express as px
from src.dao.vessels_dao import VesselsDAO
from src.dao.dockings_dao import DockingsDAO
from src.dao.payments_dao import PaymentsDAO
from src.dao.violations_dao import ViolationsDAO
from src.dao.base_dao import BaseDAO
from src.utils.supabase_client import supabase


class Dashboard:
    def __init__(self):
        self.vessels_dao = VesselsDAO(supabase)
        self.dockings_dao = DockingsDAO(supabase)
        self.payments_dao = PaymentsDAO(supabase)
        self.violations_dao = ViolationsDAO(supabase)

    def vessel_type_distribution(self):
        res = self.vessels_dao.select()
        if not res:
            return None
        df = pd.DataFrame(res)
        if "vessel_type" not in df:
            return None
        fig = px.pie(df, names="vessel_type", title="Vessel Type Distribution")
        return fig

    def dock_occupancy(self):
        res = self.dockings_dao.select()
        if not res:
            return None
        df = pd.DataFrame(res)
        if "status" not in df:
            return None
        fig = px.histogram(df, x="dock_location", color="status", title="Dock Occupancy")
        return fig

    def revenue_over_time(self):
        res = self.payments_dao.select()
        if not res:
            return None
        df = pd.DataFrame(res)
        if "payment_date" not in df:
            return None
        df["payment_date"] = pd.to_datetime(df["payment_date"])
        fig = px.line(
            df,
            x="payment_date",
            y="amount",
            title="Revenue Over Time",
        )
        return fig

    def violations_by_type(self):
        res = self.violations_dao.select()
        if not res:
            return None
        df = pd.DataFrame(res)
        if "violation_type" not in df:
            return None
        fig = px.bar(df, x="violation_type", title="Violations by Type")
        return fig
