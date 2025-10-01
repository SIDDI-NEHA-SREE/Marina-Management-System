import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk
from datetime import datetime

# --- Import Services ---
from src.services.owners_service import OwnersService
from src.services.vessels_service import VesselsService
from src.services.dockings_service import DockingsService
from src.services.payments_service import PaymentsService
from src.services.violations_service import ViolationsService
from src.services.staff_service import StaffService

# ------------------- Page Config -------------------
st.set_page_config(page_title="Marina Management System", layout="wide")

# Header
st.markdown(
    "<h2 style='text-align: center; color: white; background-color:#006D77; padding:15px; border-radius:8px;'>"
    "MARINA MANAGEMENT SYSTEM 🚤</h2>",
    unsafe_allow_html=True
)

# --- Init Services ---
owners_service = OwnersService()
vessels_service = VesselsService()
dockings_service = DockingsService()
payments_service = PaymentsService()
violations_service = ViolationsService()

# ================= Dashboard Layout =================
st.markdown("### Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

# 1. Berth Occupancy %
dockings = dockings_service.list_dockings()
occupancy = 0
if dockings:
    occupied = sum(1 for d in dockings if d.get("status") == "occupied")
    total = len(dockings)
    occupancy = round((occupied / total) * 100, 2)
col1.metric("Berth Occupancy", f"{occupancy} %")

# 2. Vessels Docked
vessels = vessels_service.list_vessels()
col2.metric("Vessels Curr. Docked", len(vessels))

# 3. Pending Payments
payments = payments_service.list_payments()
pending_amt = sum(p.get("amount", 0) for p in payments if p.get("status") == "pending")
col3.metric("Pending Payments", f"${pending_amt:,.2f}")

# 4. Active Violations
violations = violations_service.list_violations()
col4.metric("Active Violations", len(violations))

st.markdown("---")

# ================= Second Row =================
left, right = st.columns([2, 1])

# --- Vessel Activity Map ---
with left:
    st.subheader("Vessel Activity")
    if vessels:
        df_map = pd.DataFrame([
            {"lat": v.get("latitude", 17.3850), "lon": v.get("longitude", 78.4867), "name": v.get("vessel_name", "Vessel")}
            for v in vessels
        ])
        st.pydeck_chart(pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state=pdk.ViewState(latitude=17.3850, longitude=78.4867, zoom=10, pitch=50),
            layers=[
                pdk.Layer(
                    "ScatterplotLayer",
                    data=df_map,
                    get_position="[lon, lat]",
                    get_color="[0, 128, 255, 160]",
                    get_radius=200,
                ),
            ],
        ))
    else:
        st.info("No vessel location data available.")

# --- Compliance & Security Pie ---
with right:
    st.subheader("Compliance & Security")
    if violations:
        df_vio = pd.DataFrame(violations)
        counts = df_vio["violation_type"].value_counts().reset_index()
        counts.columns = ["Violation", "Count"]
        fig = px.pie(counts, names="Violation", values="Count", color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No compliance data.")

st.markdown("---")

# ================= Third Row =================
colA, colB = st.columns(2)

# --- Recent Arrivals/Departures ---
with colA:
    st.subheader("Recent Arrivals / Departures")
    if dockings:
        df_dock = pd.DataFrame(dockings)
        if "arrival_time" in df_dock.columns:
            df_dock["arrival_time"] = pd.to_datetime(df_dock["arrival_time"], errors="coerce")
        df_dock = df_dock[["vessel_id", "dock_location", "status", "arrival_time"]].sort_values("arrival_time", ascending=False)
        st.dataframe(df_dock.head(6))
    else:
        st.info("No docking records available.")

# --- Revenue Trend ---
with colB:
    st.subheader("Revenue Trend")
    if payments:
        df_pay = pd.DataFrame(payments)
        if "payment_date" in df_pay.columns:
            df_pay["payment_date"] = pd.to_datetime(df_pay["payment_date"], errors="coerce")
        revenue = df_pay.groupby(df_pay["payment_date"].dt.date)["amount"].sum().reset_index()
        fig = px.line(revenue, x="payment_date", y="amount", markers=True, title="Revenue Over Time",
                      color_discrete_sequence=["#006D77"])
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No payment records yet.")
