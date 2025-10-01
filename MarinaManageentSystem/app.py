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

st.set_page_config(page_title="Marina Management System", layout="wide")

st.title("Marina Management System 🚤")

page = st.sidebar.selectbox("Menu", [
    "Dashboard", "Owners", "Vessels", "Dockings", "Payments", "Violations", "Staff"
])

# ========== Owners ==========
if page == "Owners":
    st.header("Owners")
    service = OwnersService()

    action = st.radio("Action", ["Add", "Update", "Delete", "View"])

    if action == "Add":
        with st.form("add_owner"):
            name = st.text_input("Name")
            address = st.text_input("Address")
            phone = st.text_input("Phone")
            email = st.text_input("Email")
            submitted = st.form_submit_button("Add Owner")
            if submitted:
                res = service.create_owner(Owner(name, address, phone, email))
                st.success("Owner added!")

    elif action == "Update":
        owners = service.list_owners()
        if owners:
            df = pd.DataFrame(owners)
            owner_id = st.selectbox("Select Owner ID", df["owner_id"])
            new_address = st.text_input("New Address")
            if st.button("Update"):
                service.update_owner(owner_id, {"address": new_address})
                st.success("Owner updated!")

    elif action == "Delete":
        owners = service.list_owners()
        if owners:
            df = pd.DataFrame(owners)
            owner_id = st.selectbox("Select Owner ID to delete", df["owner_id"])
            if st.button("Delete"):
                service.delete_owner(owner_id)
                st.success("Owner deleted!")

    elif action == "View":
        owners = service.list_owners()
        st.dataframe(pd.DataFrame(owners))

# ========== Vessels ==========
if page == "Vessels":
    st.header("Vessels")
    service = VesselsService()
    action = st.radio("Action", ["Add", "Update", "Delete", "View"])

    if action == "Add":
        with st.form("add_vessel"):
            vessel_name = st.text_input("Vessel Name")
            vessel_type = st.text_input("Vessel Type")
            capacity = st.number_input("Capacity", min_value=0)
            owner_id = st.number_input("Owner ID", min_value=1)
            reg = st.text_input("Registration Number")
            submitted = st.form_submit_button("Add Vessel")
            if submitted:
                res = service.create_vessel(
                    Vessel(vessel_name, vessel_type, capacity, owner_id, reg)
                )
                st.success("Vessel added!")

    elif action == "Update":
        vessels = service.list_vessels()
        if vessels:
            df = pd.DataFrame(vessels)
            vessel_id = st.selectbox("Select Vessel ID", df["vessel_id"])
            new_type = st.text_input("New Vessel Type")
            if st.button("Update"):
                service.update_vessel(vessel_id, {"vessel_type": new_type})
                st.success("Vessel updated!")

    elif action == "Delete":
        vessels = service.list_vessels()
        if vessels:
            df = pd.DataFrame(vessels)
            vessel_id = st.selectbox("Select Vessel ID to delete", df["vessel_id"])
            if st.button("Delete"):
                service.delete_vessel(vessel_id)
                st.success("Vessel deleted!")

    elif action == "View":
        vessels = service.list_vessels()
        st.dataframe(pd.DataFrame(vessels))

# ========== Dockings ==========
if page == "Dockings":
    st.header("Dockings")
    service = DockingsService()
    action = st.radio("Action", ["Add", "Update", "Delete", "View"])

    if action == "Add":
        with st.form("add_docking"):
            vessel_id = st.number_input("Vessel ID", min_value=1)
            location = st.text_input("Dock Location")
            capacity = st.number_input("Dock Capacity", min_value=1)
            submitted = st.form_submit_button("Add Docking")
            if submitted:
                res = service.dock_vessel(Docking(vessel_id, location, capacity))
                st.success("Docking added!")

    elif action == "Update":
        dockings = service.list_dockings()
        if dockings:
            df = pd.DataFrame(dockings)
            docking_id = st.selectbox("Select Docking ID", df["docking_id"])
            new_status = st.text_input("New Status")
            if st.button("Update"):
                service.update_docking(docking_id, {"status": new_status})
                st.success("Docking updated!")

    elif action == "Delete":
        dockings = service.list_dockings()
        if dockings:
            df = pd.DataFrame(dockings)
            docking_id = st.selectbox("Select Docking ID to delete", df["docking_id"])
            if st.button("Delete"):
                service.delete_docking(docking_id)
                st.success("Docking deleted!")

    elif action == "View":
        dockings = service.list_dockings()
        st.dataframe(pd.DataFrame(dockings))

# ========== Payments ==========
if page == "Payments":
    st.header("Payments")
    service = PaymentsService()
    action = st.radio("Action", ["Add", "View"])

    if action == "Add":
        with st.form("add_payment"):
            vessel_id = st.number_input("Vessel ID", min_value=1)
            amount = st.number_input("Amount", min_value=0.0)
            ptype = st.text_input("Payment Type")
            tax = st.number_input("Tax Amount", min_value=0.0)
            submitted = st.form_submit_button("Add Payment")
            if submitted:
                res = service.record_payment(Payment(vessel_id, amount, ptype, tax))
                st.success("Payment added!")

    elif action == "View":
        payments = service.list_payments()
        st.dataframe(pd.DataFrame(payments))

# ========== Violations ==========
if page == "Violations":
    st.header("Violations")
    service = ViolationsService()
    action = st.radio("Action", ["Add", "View"])

    if action == "Add":
        with st.form("add_violation"):
            vessel_id = st.number_input("Vessel ID", min_value=1)
            vtype = st.text_input("Violation Type")
            details = st.text_area("Details")
            submitted = st.form_submit_button("Add Violation")
            if submitted:
                res = service.report_violation(Violation(vessel_id, vtype, details))
                st.success("Violation reported!")

    elif action == "View":
        violations = service.list_violations()
        st.dataframe(pd.DataFrame(violations))

# ========== Staff ==========
if page == "Staff":
    st.header("Staff")
    service = StaffService()
    action = st.radio("Action", ["Add", "Update", "Delete", "View"])

    if action == "Add":
        with st.form("add_staff"):
            name = st.text_input("Name")
            role = st.text_input("Role")
            contact = st.text_input("Contact Info")
            submitted = st.form_submit_button("Add Staff")
            if submitted:
                res = service.add_staff(Staff(name, role, contact))
                st.success("Staff added!")

    elif action == "Update":
        staff = service.list_staff()
        if staff:
            df = pd.DataFrame(staff)
            staff_id = st.selectbox("Select Staff ID", df["staff_id"])
            new_role = st.text_input("New Role")
            if st.button("Update"):
                service.update_staff(staff_id, {"role": new_role})
                st.success("Staff updated!")

    elif action == "Delete":
        staff = service.list_staff()
        if staff:
            df = pd.DataFrame(staff)
            staff_id = st.selectbox("Select Staff ID to delete", df["staff_id"])
            if st.button("Delete"):
                service.delete_staff(staff_id)
                st.success("Staff deleted!")

    elif action == "View":
        staff = service.list_staff()
        st.dataframe(pd.DataFrame(staff))

# ========== Dashboard ==========
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
