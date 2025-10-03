import plotly.express as px
import pandas as pd
from src.services.vessels_service import VesselsService
from src.services.dockings_service import DockingsService
from src.services.payments_service import PaymentsService
from src.services.violations_service import ViolationsService

class Dashboard:
    def __init__(self):
        self.vessels_service = VesselsService()
        self.dockings_service = DockingsService()
        self.payments_service = PaymentsService()
        self.violations_service = ViolationsService()

    def vessel_type_distribution(self):
        data = self.vessels_service.list_vessels()
        if not data: return None
        df = pd.DataFrame(data)
        return px.pie(df, names="vessel_type", title="Vessel Types")
    def dock_occupancy(self):
        data = self.dockings_service.list_dockings()
        if not data: return None
        df = pd.DataFrame(data)
        return px.histogram(df, x="status", title="Dock Occupancy")

    def revenue_over_time(self):
        data = self.payments_service.list_payments()
        if not data: return None
        df = pd.DataFrame(data)
        df["payment_date"] = pd.to_datetime(df["payment_date"])
        return px.line(df, x="payment_date", y="amount", title="Revenue Over Time")

    def violations_alerts(self):
        data = self.violations_service.list_violations()
        if not data: return None
        return pd.DataFrame(data)

    def vessel_map(self):
        data = pd.DataFrame([
            {"vessel": "Vessel A", "lat": 17.385044, "lon": 78.486671},
            {"vessel": "Vessel B", "lat": 13.0827, "lon": 80.2707},
            {"vessel": "Vessel C", "lat": 19.0760, "lon": 72.8777},
        ])
        return px.scatter_mapbox(data, lat="lat", lon="lon", text="vessel",
                                 zoom=4, height=500, mapbox_style="open-street-map",
                                 title="Vessel Activity Map")


