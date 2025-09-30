import streamlit as st
import pandas as pd
from src.services.owners_service import OwnersService
from src.models.owner import Owner
from src.dashboard.dashboard import Dashboard


st.set_page_config(page_title="Marina Management System", layout="wide")

st.title("Marina Management System 🚤")

page = st.sidebar.selectbox("Menu", [
    "Dashboard", "Owners", "Vessels", "Dockings", "Payments", "Violations", "Staff"
])

# --- Owners Page ---
if page == "Owners":
    st.header("Owners")
    with st.form("owner_form"):
        name = st.text_input("Name")
        address = st.text_input("Address")
        phone = st.text_input("Phone")
        email = st.text_input("Email")
        submitted = st.form_submit_button("Add Owner")
        if submitted:
            service = OwnersService()
            o = Owner(name, address, phone, email)
            res = service.create_owner(o)
            st.success("Owner added!" if not res.error else f"Error: {res.error}")

    # Owners List
    st.subheader("Owners List")
    service = OwnersService()
    owners = service.list_owners()
    st.dataframe(pd.DataFrame(owners))

# --- Dashboard Page ---
if page == "Dashboard":
    st.header("📊 Marina Dashboard")
    dashboard = Dashboard()

    col1, col2 = st.columns(2)
    with col1:
        fig1 = dashboard.vessel_type_distribution()
        if fig1:
            st.plotly_chart(fig1, use_container_width=True)
    with col2:
        fig2 = dashboard.dock_occupancy()
        if fig2:
            st.plotly_chart(fig2, use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        fig3 = dashboard.revenue_over_time()
        if fig3:
            st.plotly_chart(fig3, use_container_width=True)
    with col4:
        fig4 = dashboard.violations_by_type()
        if fig4:
            st.plotly_chart(fig4, use_container_width=True)
