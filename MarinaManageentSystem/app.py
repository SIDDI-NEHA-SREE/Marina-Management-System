import streamlit as st
import pandas as pd

from src.services.owners_service import OwnersService
from src.services.vessels_service import VesselsService
from src.services.dockings_service import DockingsService
from src.services.payments_service import PaymentsService
from src.services.violations_service import ViolationsService
from src.services.staff_service import StaffService

from src.models.owner import Owner
from src.models.vessel import Vessel
from src.models.docking import Docking
from src.models.payment import Payment
from src.models.violation import Violation
from src.models.staff import Staff

from src.dashboard.dashboard import Dashboard

# --- Page Config ---
st.set_page_config(page_title="Marina Management System 🚤", layout="wide")

# --- Custom Styling ---
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(120deg, #e6f7ff 0%, #ffffff 100%);
    }
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #004080 0%, #0077b6 100%);
        color: white;
    }
    section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] label {
        color: white !important;
    }
    /* Headers */
    h1, h2, h3 {
        color: #003366;
    }
    /* Forms */
    .stForm {
        border: 2px solid #0077b6;
        padding: 15px;
        border-radius: 10px;
        background-color: #f0f8ff;
    }
    /* Buttons */
    div.stButton > button {
        background-color: #0077b6;
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #005f8c;
        color: #f0f8ff;
    }
    /* DataFrame Table */
    .dataframe {
        border: 1px solid #0077b6;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("🌊 Marina Management System 🚤")

# --- Sidebar Menu ---
page = st.sidebar.selectbox("📌 Menu", [
    "Dashboard", "Owners", "Vessels", "Dockings", "Payments", "Violations", "Staff"
])

# ---------------- Owners ----------------
if page == "Owners":
    st.header("👤 Owners Management")
    service = OwnersService()
    action = st.selectbox("Choose Action", ["Add", "Update", "Delete", "View"])

    if action == "Add":
        with st.form("add_owner"):
            name = st.text_input("Name")
            address = st.text_input("Address")
            phone = st.text_input("Phone")
            email = st.text_input("Email")
            submitted = st.form_submit_button("➕ Add Owner")
            if submitted:
                service.create_owner(Owner(name, address, phone, email))
                st.success("✅ Owner added!")

    elif action == "Update":
        owners = service.list_owners()
        if owners:
            df = pd.DataFrame(owners)
            owner_id = st.selectbox("Select Owner ID", df["owner_id"])
            new_address = st.text_input("New Address")
            if st.button("🔄 Update Owner"):
                service.update_owner(owner_id, {"address": new_address})
                st.success("✅ Owner updated!")

    elif action == "Delete":
        owners = service.list_owners()
        if owners:
            df = pd.DataFrame(owners)
            owner_id = st.selectbox("Select Owner ID", df["owner_id"])
            if st.button("❌ Delete Owner"):
                service.delete_owner(owner_id)
                st.success("✅ Owner deleted!")

    elif action == "View":
        st.dataframe(pd.DataFrame(service.list_owners()))

# ---------------- Dashboard ----------------
if page == "Dashboard":
    st.header("📊 Marina Dashboard")
    dashboard = Dashboard()

    col1, col2 = st.columns(2)
    with col1:
        try:
            st.plotly_chart(dashboard.vessel_type_distribution(), use_container_width=True)
        except Exception as e:
            st.error(f"Error: {e}")
    with col2:
        try:
            st.plotly_chart(dashboard.dock_occupancy(), use_container_width=True)
        except Exception as e:
            st.error(f"Error: {e}")

    col3, col4 = st.columns(2)
    with col3:
        try:
            st.plotly_chart(dashboard.revenue_over_time(), use_container_width=True)
        except Exception as e:
            st.error(f"Error: {e}")
    with col4:
        try:
            st.plotly_chart(dashboard.violations_by_type(), use_container_width=True)
        except Exception as e:
            st.error(f"Error: {e}")

