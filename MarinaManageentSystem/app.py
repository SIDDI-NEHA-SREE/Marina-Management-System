import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Services
from src.services.owners_service import OwnersService
from src.services.vessels_service import VesselsService
from src.services.dockings_service import DockingsService
from src.services.payments_service import PaymentsService
from src.services.violations_service import ViolationsService
from src.services.staff_service import StaffService

# Models
from src.models.owner import Owner
from src.models.vessel import Vessel
from src.models.docking import Docking
from src.models.payment import Payment
from src.models.violation import Violation
from src.models.staff import Staff

# Dashboard
from src.dashboard.dashboard import Dashboard


# ------------- Page Config & Styles -------------
st.set_page_config(page_title="Marina Management System", layout="wide")

st.markdown(
    """
    <style>
        body {background-color: #e6f7ff;}
        .main {background-color: #f8fcff;}
        h1, h2, h3, h4 {
            color: #003366 !important;
            font-family: 'Arial Black', sans-serif;
        }
        .stButton button {
            background-color: #0077b6;
            color: white;
            border-radius: 8px;
            padding: 8px 16px;
        }
        .stButton button:hover {
            background-color: #005f8a;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🌊 Marina Management System 🚤")

page = st.sidebar.selectbox(
    "Menu",
    ["Dashboard", "Owners", "Vessels", "Dockings", "Payments", "Violations", "Staff"],
)


# ------------- Owners -------------
if page == "Owners":
    st.header("👤 Owners")
    service = OwnersService()
    action = st.selectbox("Choose Action", ["Add", "Update", "Delete", "View"])

    if action == "Add":
        with st.form("add_owner"):
            name = st.text_input("Name")
            address = st.text_input("Address")
            phone = st.text_input("Phone")
            email = st.text_input("Email")
            submitted = st.form_submit_button("Add Owner")
            if submitted:
                service.create_owner(Owner(name, address, phone, email))
                st.success("✅ Owner added!")

    elif action == "Update":
        owners = service.list_owners()
        if owners:
            df = pd.DataFrame(owners)
            owner_id = st.selectbox("Select Owner ID", df["owner_id"])
            new_address = st.text_input("New Address")
            if st.button("Update"):
                service.update_owner(owner_id, {"address": new_address})
                st.success("✅ Owner updated!")

    elif action == "Delete":
        owners = service.list_owners()
        if owners:
            df = pd.DataFrame(owners)
            owner_id = st.selectbox("Select Owner ID", df["owner_id"])
            if st.button("Delete"):
                service.delete_owner(owner_id)
                st.success("🗑️ Owner deleted!")

    elif action == "View":
        st.dataframe(pd.DataFrame(service.list_owners()))


# ------------- Vessels -------------
if page == "Vessels":
    st.header("🚤 Vessels")
    service = VesselsService()
    action = st.selectbox("Choose Action", ["Add", "Update", "Delete", "View"])

    if action == "Add":
        with st.form("add_vessel"):
            vessel_name = st.text_input("Vessel Name")
            vessel_type = st.text_input("Vessel Type")
            capacity = st.number_input("Capacity", min_value=0)
            owner_id = st.number_input("Owner ID", min_value=1)
            reg = st.text_input("Registration Number")
            submitted = st.form_submit_button("Add Vessel")
            if submitted:
                service.create_vessel(Vessel(vessel_name, vessel_type, capacity, owner_id, reg))
                st.success("✅ Vessel added!")

    elif action == "Update":
        vessels = service.list_vessels()
        if vessels:
            df = pd.DataFrame(vessels)
            vessel_id = st.selectbox("Select Vessel ID", df["vessel_id"])
            new_type = st.text_input("New Vessel Type")
            if st.button("Update"):
                service.update_vessel(vessel_id, {"vessel_type": new_type})
                st.success("✅ Vessel updated!")

    elif action == "Delete":
        vessels = service.list_vessels()
        if vessels:
            df = pd.DataFrame(vessels)
            vessel_id = st.selectbox("Select Vessel ID", df["vessel_id"])
            if st.button("Delete"):
                service.delete_vessel(vessel_id)
                st.success("🗑️ Vessel deleted!")

    elif action == "View":
        st.dataframe(pd.DataFrame(service.list_vessels()))


# ------------- Dockings -------------
if page == "Dockings":
    st.header("⚓ Dockings")
    service = DockingsService()
    action = st.selectbox("Choose Action", ["Add", "Update", "Delete", "View"])

    if action == "Add":
        with st.form("add_docking"):
            vessel_id = st.number_input("Vessel ID", min_value=1)
            location = st.text_input("Dock Location")
            capacity = st.number_input("Dock Capacity", min_value=1)
            submitted = st.form_submit_button("Add Docking")
            if submitted:
                service.dock_vessel(Docking(vessel_id, location, capacity))
                st.success("✅ Docking added!")

    elif action == "Update":
        dockings = service.list_dockings()
        if dockings:
            df = pd.DataFrame(dockings)
            docking_id = st.selectbox("Select Docking ID", df["docking_id"])
            new_status = st.text_input("New Status")
            if st.button("Update"):
                service.update_docking(docking_id, {"status": new_status})
                st.success("✅ Docking updated!")

    elif action == "Delete":
        dockings = service.list_dockings()
        if dockings:
            df = pd.DataFrame(dockings)
            docking_id = st.selectbox("Select Docking ID", df["docking_id"])
            if st.button("Delete"):
                service.delete_docking(docking_id)
                st.success("🗑️ Docking deleted!")

    elif action == "View":
        st.dataframe(pd.DataFrame(service.list_dockings()))


# ------------- Payments -------------
if page == "Payments":
    st.header("💰 Payments")
    service = PaymentsService()
    action = st.selectbox("Choose Action", ["Add", "View"])

    if action == "Add":
        with st.form("add_payment"):
            vessel_id = st.number_input("Vessel ID", min_value=1)
            amount = st.number_input("Amount", min_value=0.0)
            ptype = st.text_input("Payment Type")
            tax = st.number_input("Tax Amount", min_value=0.0)
            submitted = st.form_submit_button("Add Payment")
            if submitted:
                service.record_payment(Payment(vessel_id, amount, ptype, tax))
                st.success("✅ Payment recorded!")

    elif action == "View":
        payments = service.list_payments()
        df = pd.DataFrame(payments)
        if "payment_date" in df.columns:
            df["payment_date"] = pd.to_datetime(df["payment_date"])
        st.dataframe(df)


# ------------- Violations -------------
if page == "Violations":
    st.header("⚠️ Violations")
    service = ViolationsService()
    mode = st.radio("Violation Entry Mode", ["Manual", "Automated"])

    if mode == "Manual":
        with st.form("add_violation"):
            vessel_id = st.number_input("Vessel ID", min_value=1)
            vtype = st.text_input("Violation Type")
            details = st.text_area("Details")
            submitted = st.form_submit_button("Report Violation")
            if submitted:
                service.report_violation(Violation(vessel_id, vtype, details))
                st.success("✅ Violation reported manually!")

    elif mode == "Automated":
        st.info("GPS-based violation detection (demo)")
        gps_data = [
            {"vessel_id": 1, "lat": 17.3850, "lon": 78.4867},
            {"vessel_id": 2, "lat": 13.0827, "lon": 80.2707},
        ]
        for v in gps_data:
            if v["lat"] > 17.0:  # demo condition
                service.report_violation(Violation(v["vessel_id"], "Speeding", "Exceeded limits"))
        st.success("✅ Automated violations checked and recorded!")


# ------------- Staff -------------
if page == "Staff":
    st.header("👨‍✈️ Staff")
    service = StaffService()
    action = st.selectbox("Choose Action", ["Add", "Update", "Delete", "View"])

    if action == "Add":
        with st.form("add_staff"):
            name = st.text_input("Name")
            role = st.text_input("Role")
            contact = st.text_input("Contact Info")
            submitted = st.form_submit_button("Add Staff")
            if submitted:
                service.add_staff(Staff(name, role, contact))
                st.success("✅ Staff added!")

    elif action == "Update":
        staff = service.list_staff()
        if staff:
            df = pd.DataFrame(staff)
            staff_id = st.selectbox("Select Staff ID", df["staff_id"])
            new_role = st.text_input("New Role")
            if st.button("Update"):
                service.update_staff(staff_id, {"role": new_role})
                st.success("✅ Staff updated!")

    elif action == "Delete":
        staff = service.list_staff()
        if staff:
            df = pd.DataFrame(staff)
            staff_id = st.selectbox("Select Staff ID", df["staff_id"])
            if st.button("Delete"):
                service.delete_staff(staff_id)
                st.success("🗑️ Staff deleted!")

    elif action == "View":
        st.dataframe(pd.DataFrame(service.list_staff()))


# ------------- Dashboard -------------
if page == "Dashboard":
    st.markdown(
        "<h1 style='text-align: center; color: #003366;'>📊 Marina Dashboard</h1>",
        unsafe_allow_html=True
    )

    # Vessel map
    st.subheader("🌍 Vessel Locations")
    m = folium.Map(location=[16.5, 80.6], zoom_start=5, tiles="CartoDB dark_matter")

    gps_data = [
        {"vessel_id": 1, "lat": 17.3850, "lon": 78.4867},
        {"vessel_id": 2, "lat": 13.0827, "lon": 80.2707},
        {"vessel_id": 3, "lat": 18.1124, "lon": 83.3956},
    ]

    for v in gps_data:
        folium.Marker(
            [v["lat"], v["lon"]],
            popup=f"<b>Vessel {v['vessel_id']}</b>",
            icon=folium.Icon(color="lightblue", icon="ship", prefix="fa"),
        ).add_to(m)

    st_folium(m, width=900, height=500)

    # Charts
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
