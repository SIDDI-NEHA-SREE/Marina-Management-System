import streamlit as st
import pandas as pd

# Import services + models
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


# ------------------- CONFIG -------------------
st.set_page_config(page_title="Marina Management System", layout="wide")
st.title("Marina Management System 🚤")

# Sidebar menu
page = st.sidebar.selectbox("Menu", [
    "Dashboard", "Owners", "Vessels", "Dockings", "Payments", "Violations", "Staff"
])


# ------------------- OWNERS -------------------
if page == "Owners":
    st.header("⚓ Owners Management")
    service = OwnersService()

    action = st.radio("Choose action:", ["Add", "Update", "Delete", "View All"])

    if action == "Add":
        with st.form("add_owner"):
            name = st.text_input("Name")
            address = st.text_input("Address")
            phone = st.text_input("Phone")
            email = st.text_input("Email")
            submitted = st.form_submit_button("Add Owner")
            if submitted:
                owner = Owner(name, address, phone, email)
                res = service.create_owner(owner)
                st.success("Owner added successfully!")

    elif action == "Update":
        owners = service.list_owners()
        if owners:
            df = pd.DataFrame(owners)
            selected = st.selectbox("Select Owner to Update", df["owner_id"])
            new_name = st.text_input("New Name")
            if st.button("Update Owner"):
                service.update_owner(selected, {"name": new_name})
                st.success("Owner updated!")

    elif action == "Delete":
        owners = service.list_owners()
        if owners:
            df = pd.DataFrame(owners)
            selected = st.selectbox("Select Owner to Delete", df["owner_id"])
            if st.button("Delete Owner"):
                service.delete_owner(selected)
                st.success("Owner deleted!")

    elif action == "View All":
        owners = service.list_owners()
        st.dataframe(pd.DataFrame(owners))


# ------------------- VESSELS -------------------
if page == "Vessels":
    st.header("⛴ Vessels Management")
    service = VesselsService()

    action = st.radio("Choose action:", ["Add", "Update", "Delete", "View All"])

    if action == "Add":
        with st.form("add_vessel"):
            name = st.text_input("Vessel Name")
            vtype = st.text_input("Type")
            capacity = st.number_input("Capacity", min_value=0)
            owner_id = st.number_input("Owner ID", min_value=1)
            reg = st.text_input("Registration Number")
            submitted = st.form_submit_button("Add Vessel")
            if submitted:
                vessel = Vessel(name, vtype, capacity, owner_id, reg)
                service.create_vessel(vessel)
                st.success("Vessel added!")

    elif action == "Update":
        vessels = service.list_vessels()
        if vessels:
            df = pd.DataFrame(vessels)
            selected = st.selectbox("Select Vessel ID", df["vessel_id"])
            new_type = st.text_input("New Type")
            if st.button("Update Vessel"):
                service.update_vessel(selected, {"vessel_type": new_type})
                st.success("Vessel updated!")

    elif action == "Delete":
        vessels = service.list_vessels()
        if vessels:
            df = pd.DataFrame(vessels)
            selected = st.selectbox("Select Vessel ID", df["vessel_id"])
            if st.button("Delete Vessel"):
                service.delete_vessel(selected)
                st.success("Vessel deleted!")

    elif action == "View All":
        vessels = service.list_vessels()
        st.dataframe(pd.DataFrame(vessels))


# ------------------- DOCKINGS -------------------
if page == "Dockings":
    st.header("🛳 Dockings")
    service = DockingsService()

    action = st.radio("Choose action:", ["Add", "View All"])

    if action == "Add":
        with st.form("add_docking"):
            vessel_id = st.number_input("Vessel ID", min_value=1)
            location = st.text_input("Dock Location")
            capacity = st.number_input("Dock Capacity", min_value=1)
            submitted = st.form_submit_button("Dock Vessel")
            if submitted:
                docking = Docking(vessel_id, location, capacity)
                service.dock_vessel(docking)
                st.success("Docking recorded!")

    elif action == "View All":
        dockings = service.list_dockings()
        st.dataframe(pd.DataFrame(dockings))


# ------------------- PAYMENTS -------------------
if page == "Payments":
    st.header("💰 Payments")
    service = PaymentsService()

    action = st.radio("Choose action:", ["Add", "View All"])

    if action == "Add":
        with st.form("add_payment"):
            vessel_id = st.number_input("Vessel ID", min_value=1)
            amount = st.number_input("Amount", min_value=0.0)
            ptype = st.text_input("Payment Type")
            tax = st.number_input("Tax", min_value=0.0)
            submitted = st.form_submit_button("Add Payment")
            if submitted:
                payment = Payment(vessel_id, amount, ptype, tax)
                service.record_payment(payment)
                st.success("Payment recorded!")

    elif action == "View All":
        payments = service.list_payments()
        st.dataframe(pd.DataFrame(payments))


# ------------------- VIOLATIONS -------------------
if page == "Violations":
    st.header("⚠️ Violations")
    service = ViolationsService()

    action = st.radio("Choose action:", ["Add", "View All"])

    if action == "Add":
        with st.form("add_violation"):
            vessel_id = st.number_input("Vessel ID", min_value=1)
            vtype = st.text_input("Violation Type")
            details = st.text_area("Details")
            submitted = st.form_submit_button("Report Violation")
            if submitted:
                violation = Violation(vessel_id, vtype, details)
                service.report_violation(violation)
                st.success("Violation reported!")

    elif action == "View All":
        violations = service.list_violations()
        st.dataframe(pd.DataFrame(violations))


# ------------------- STAFF -------------------
if page == "Staff":
    st.header("👨‍✈️ Staff")
    service = StaffService()

    action = st.radio("Choose action:", ["Add", "View All"])

    if action == "Add":
        with st.form("add_staff"):
            name = st.text_input("Name")
            role = st.text_input("Role")
            contact = st.text_input("Contact Info")
            submitted = st.form_submit_button("Add Staff")
            if submitted:
                staff = Staff(name, role, contact)
                service.add_staff(staff)
                st.success("Staff added!")

    elif action == "View All":
        staff = service.list_staff()
        st.dataframe(pd.DataFrame(staff))


# ------------------- DASHBOARD -------------------
if page == "Dashboard":
    st.header("📊 Marina Dashboard")
    dashboard = Dashboard()

    col1, col2 = st.columns(2)
    with col1:
        fig1 = dashboard.vessel_type_distribution()
        if fig1: st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = dashboard.dock_occupancy()
        if fig2: st.plotly_chart(fig2, use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        fig3 = dashboard.revenue_over_time()
        if fig3: st.plotly_chart(fig3, use_container_width=True)

    with col4:
        fig4 = dashboard.violations_by_type()
        if fig4: st.plotly_chart(fig4, use_container_width=True)
