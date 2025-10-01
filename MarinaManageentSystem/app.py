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
                if res:
                    st.success("Owner added!")
                else:
                    st.error("Failed to add owner.")

    elif action == "Update":
        owners = service.list_owners()
        if owners:
            df = pd.DataFrame(owners)
            owner_id = st.selectbox("Select Owner ID", df["owner_id"])
            new_address = st.text_input("New Address")
            if st.button("Update"):
                res = service.update_owner(owner_id, {"address": new_address})
                if res:
                    st.success("Owner updated!")
                else:
                    st.error("Failed to update owner.")

    elif action == "Delete":
        owners = service.list_owners()
        if owners:
            df = pd.DataFrame(owners)
            owner_id = st.selectbox("Select Owner to Delete", df["owner_id"])
            if st.button("Delete"):
                res = service.delete_owner(owner_id)
                if res:
                    st.success("Owner deleted!")
                else:
                    st.error("Failed to delete owner.")

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
                res = service.create_vessel(Vessel(vessel_name, vessel_type, capacity, owner_id, reg))
                if res:
                    st.success("Vessel added!")
                else:
                    st.error("Failed to add vessel.")

    elif action == "Update":
        vessels = service.list_vessels()
        if vessels:
            df = pd.DataFrame(vessels)
            vessel_id = st.selectbox("Select Vessel ID", df["vessel_id"])
            new_type = st.text_input("New Vessel Type")
            if st.button("Update"):
                res = service.update_vessel(vessel_id, {"vessel_type": new_type})
                if res:
                    st.success("Vessel updated!")
                else:
                    st.error("Failed to update vessel.")

    elif action == "Delete":
        vessels = service.list_vessels()
        if vessels:
            df = pd.DataFrame(vessels)
            vessel_id = st.selectbox("Select Vessel to Delete", df["vessel_id"])
            if st.button("Delete"):
                res = service.delete_vessel(vessel_id)
                if res:
                    st.success("Vessel deleted!")
                else:
                    st.error("Failed to delete vessel.")

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
                if res:
                    st.success("Docking added!")
                else:
                    st.error("Failed to add docking.")

    elif action == "Update":
        dockings = service.list_dockings()
        if dockings:
            df = pd.DataFrame(dockings)
            docking_id = st.selectbox("Select Docking ID", df["docking_id"])
            new_status = st.text_input("New Status")
            if st.button("Update"):
                res = service.update_docking(docking_id, {"status": new_status})
                if res:
                    st.success("Docking updated!")
                else:
                    st.error("Failed to update docking.")

    elif action == "Delete":
        dockings = service.list_dockings()
        if dockings:
            df = pd.DataFrame(dockings)
            docking_id = st.selectbox("Select Docking to Delete", df["docking_id"])
            if st.button("Delete"):
                res = service.delete_docking(docking_id)
                if res:
                    st.success("Docking deleted!")
                else:
                    st.error("Failed to delete docking.")

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
                if res:
                    st.success("Payment added!")
                else:
                    st.error("Failed to add payment.")

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
                if res:
                    st.success("Violation reported!")
                else:
                    st.error("Failed to add violation.")

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
                if res:
                    st.success("Staff added!")
                else:
                    st.error("Failed to add staff.")

    elif action == "Update":
        staff = service.list_staff()
        if staff:
            df = pd.DataFrame(staff)
            staff_id = st.selectbox("Select Staff", df["staff_id"])
            new_role = st.text_input("New Role")
            if st.button("Update"):
                res = service.update_staff(staff_id, {"role": new_role})
                if res:
                    st.success("Staff updated!")
                else:
                    st.error("Failed to update staff.")

    elif action == "Delete":
        staff = service.list_staff()
        if staff:
            df = pd.DataFrame(staff)
            staff_id = st.selectbox("Select Staff to Delete", df["staff_id"])
            if st.button("Delete"):
                res = service.delete_staff(staff_id)
                if res:
                    st.success("Staff deleted!")
                else:
                    st.error("Failed to delete staff.")

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
        else:
            st.info("No vessel data yet.")

    with col2:
        fig2 = dashboard.dock_occupancy()
        if fig2:
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info("No docking data yet.")

    col3, col4 = st.columns(2)
    with col3:
        fig3 = dashboard.revenue_over_time()
        if fig3:
            st.plotly_chart(fig3, use_container_width=True)
        else:
            st.info("No payment data yet.")

    with col4:
        fig4 = dashboard.violations_by_type()
        if fig4:
            st.plotly_chart(fig4, use_container_width=True)
        else:
            st.info("No violation data yet.")
