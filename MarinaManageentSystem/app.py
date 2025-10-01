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

# ---------------- Page Config ----------------
st.set_page_config(page_title="Marina Management System", layout="wide")

# ---------------- Custom CSS ----------------
st.markdown("""
    <style>
    /* General Background */
    .stApp {
        background-color: #fdfdfd;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #006D77;
        color: white;
    }
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] div {
        color: white !important;
        font-weight: bold;
    }

    /* Headers */
    h1 {
        color: #006D77;
        font-size: 2.2em;
        font-weight: bold;
    }
    h2 {
        color: #006D77;
        margin-top: 20px;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #006D77;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #004E52;
        color: #FFDD67;
    }

    /* Forms */
    .stForm {
        border: 2px solid #83C5BE;
        padding: 20px;
        border-radius: 12px;
        background-color: #f5fcfc;
    }

    /* Info Boxes */
    .info-card {
        background-color: #83C5BE;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        color: #004E52;
        font-weight: bold;
        font-size: 1.2em;
    }

    /* Alerts */
    .stSuccess {
        background-color: #FFDD67 !important;
        color: black !important;
        border-radius: 6px;
        padding: 10px;
    }
    .stError {
        background-color: #B23A48 !important;
        color: white !important;
        border-radius: 6px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------
st.title("🌊 Marina Management System 🚤")

# ---------------- Sidebar Menu ----------------
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
        owners = service.list_owners()
        st.subheader("📋 Owners List")
        st.dataframe(pd.DataFrame(owners))

# ---------------- Dashboard ----------------
if page == "Dashboard":
    st.header("📊 Marina Dashboard")
    dashboard = Dashboard()

    # Top summary metrics
    colA, colB, colC = st.columns(3)
    colA.markdown('<div class="info-card">🚢 Total Vessels</div>', unsafe_allow_html=True)
    colB.markdown('<div class="info-card">⚓ Active Dockings</div>', unsafe_allow_html=True)
    colC.markdown('<div class="info-card">💰 Total Revenue</div>', unsafe_allow_html=True)

    # Graphs
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
