import streamlit as st
import pandas as pd

# Import models
from src.models.owner import Owner
from src.models.vessel import Vessel
from src.models.docking import Docking
from src.models.payment import Payment
from src.models.violation import Violation
from src.models.staff import Staff

# Import services
from src.services.owners_service import OwnersService
from src.services.vessels_service import VesselsService
from src.services.dockings_service import DockingsService
from src.services.payments_service import PaymentsService
from src.services.violations_service import ViolationsService
from src.services.staff_service import StaffService

# Dashboard
from src.dashboard.dashboard import Dashboard


st.set_page_config(page_title="Marina Management System", layout="wide")
st.title("Marina Management System 🚤")

page = st.sidebar.selectbox("Menu", [
    "Dashboard", "Owners", "Vessels", "Dockings", "Payments", "Violations", "Staff"
])

# ==========================================================
# Owners Page
# ==========================================================
if page == "Owners":
    st.header("Owners")
    action = st.selectbox("Choose Action", ["View All", "Add", "Update", "Delete"])
    service = OwnersService()

    if action == "Add":
        with st.form("add_owner"):
            name = st.text_input("Name")
            address = st.text_input("Address")
            phone = st.text_input("Phone")
            email = st.text_input("Email")
            submitted = st.form_submit_button("Add Owner")
            if submitted:
                o = Owner(name, address, phone, email)
                res = service.create_owner(o)
                if res.data:
                    st.success("Owner added!")
                else:
                    st.error("Failed to add owner.")

    elif action == "Update":
        owners = service.list_owners()
        df = pd.DataFrame(owners)
        if not df.empty:
            owner_id = st.selectbox("Select Owner ID", df["owner_id"])
            name = st.text_input("Name")
            address = st.text_input("Address")
            phone = st.text_input("Phone")
            email = st.text_input("Email")
            if st.button("Update Owner"):
                res = service.dao.update(owner_id, {
                    "name": name,
                    "address": address,
                    "phone": phone,
                    "email": email
                })
                if res.data:
                    st.success("Owner updated!")
                else:
                    st.error("Failed to update owner.")

    elif action == "Delete":
        owners = service.list_owners()
        df = pd.DataFrame(owners)
        if not df.empty:
            owner_id = st.selectbox("Select Owner ID", df["owner_id"])
            if st.button("Delete Owner"):
                res = service.dao.delete(owner_id)
                if res.data:
                    st.success("Owner deleted!")
                else:
                    st.error("Failed to delete owner.")

    st.subheader("Owners List")
    st.dataframe(pd.DataFrame(service.list_owners()))


# ==========================================================
# Vessels Page
# ==========================================================
if page == "Vessels":
    st.header("Vessels")
    action = st.selectbox("Choose Action", ["View All", "Add", "Update", "Delete"])
    service = VesselsService()

    if action == "Add":
        with st.form("add_vessel"):
            vessel_name = st.text_input("Vessel Name")
            vessel_type = st.text_input("Vessel Type")
            capacity = st.number_input("Capacity", min_value=0, step=1)
            owner_id = st.number_input("Owner ID", min_value=1, step=1)
            reg = st.text_input("Registration Number")
            submitted = st.form_submit_button("Add Vessel")
            if submitted:
                v = Vessel(vessel_name, vessel_type, capacity, owner_id, reg)
                res = service.create_vessel(v)
                if res.data:
                    st.success("Vessel added!")
                else:
                    st.error("Failed to add vessel.")

    elif action == "Update":
        vessels = service.list_vessels()
        df = pd.DataFrame(vessels)
        if not df.empty:
            vessel_id = st.selectbox("Select Vessel ID", df["vessel_id"])
            vessel_name = st.text_input("Vessel Name")
            vessel_type = st.text_input("Vessel Type")
            capacity = st.number_input("Capacity", min_value=0, step=1)
            owner_id = st.number_input("Owner ID", min_value=1, step=1)
            reg = st.text_input("Registration Number")
            if st.button("Update Vessel"):
                res = service.dao.update(vessel_id, {
                    "vessel_name": vessel_name,
                    "vessel_type": vessel_type,
                    "capacity": capacity,
                    "owner_id": owner_id,
                    "registration_number": reg
                })
                if res.data:
                    st.success("Vessel updated!")
                else:
                    st.error("Failed to update vessel.")

    elif action == "Delete":
        vessels = service.list_vessels()
        df = pd.DataFrame(vessels)
        if not df.empty:
            vessel_id = st.selectbox("Select Vessel ID", df["vessel_id"])
            if st.button("Delete Vessel"):
                res = service.dao.delete(vessel_id)
                if res.data:
                    st.success("Vessel deleted!")
                else:
                    st.error("Failed to delete vessel.")

    st.subheader("Vessels List")
    st.dataframe(pd.DataFrame(service.list_vessels()))


# ==========================================================
# Dockings Page
# ==========================================================
if page == "Dockings":
    st.header("Dockings")
    action = st.selectbox("Choose Action", ["View All", "Add", "Delete"])
    service = DockingsService()

    if action == "Add":
        with st.form("add_docking"):
            vessel_id = st.number_input("Vessel ID", min_value=1, step=1)
            dock_location = st.text_input("Dock Location")
            dock_capacity = st.number_input("Dock Capacity", min_value=1, step=1)
            submitted = st.form_submit_button("Dock Vessel")
            if submitted:
                d = Docking(vessel_id, dock_location, dock_capacity)
                res = service.dock_vessel(d)
                if res.data:
                    st.success("Docking added!")
                else:
                    st.error("Failed to add docking.")

    elif action == "Delete":
        dockings = service.list_dockings()
        df = pd.DataFrame(dockings)
        if not df.empty:
            docking_id = st.selectbox("Select Docking ID", df["docking_id"])
            if st.button("Delete Docking"):
                res = service.dao.delete(docking_id)
                if res.data:
                    st.success("Docking deleted!")
                else:
                    st.error("Failed to delete docking.")

    st.subheader("Dockings List")
    st.dataframe(pd.DataFrame(service.list_dockings()))


# ==========================================================
# Payments Page
# ==========================================================
if page == "Payments":
    st.header("Payments")
    action = st.selectbox("Choose Action", ["View All", "Add", "Delete"])
    service = PaymentsService()

    if action == "Add":
        with st.form("add_payment"):
            vessel_id = st.number_input("Vessel ID", min_value=1, step=1)
            amount = st.number_input("Amount", min_value=0.0, step=0.01)
            ptype = st.text_input("Payment Type")
            tax = st.number_input("Tax Amount", min_value=0.0, step=0.01)
            submitted = st.form_submit_button("Record Payment")
            if submitted:
                p = Payment(vessel_id, amount, ptype, tax)
                res = service.record_payment(p)
                if res.data:
                    st.success("Payment recorded!")
                else:
                    st.error("Failed to record payment.")

    elif action == "Delete":
        payments = service.list_payments()
        df = pd.DataFrame(payments)
        if not df.empty:
            payment_id = st.selectbox("Select Payment ID", df["payment_id"])
            if st.button("Delete Payment"):
                res = service.dao.delete(payment_id)
                if res.data:
                    st.success("Payment deleted!")
                else:
                    st.error("Failed to delete payment.")

    st.subheader("Payments List")
    st.dataframe(pd.DataFrame(service.list_payments()))


# ==========================================================
# Violations Page
# ==========================================================
if page == "Violations":
    st.header("Violations")
    action = st.selectbox("Choose Action", ["View All", "Add", "Delete"])
    service = ViolationsService()

    if action == "Add":
        with st.form("add_violation"):
            vessel_id = st.number_input("Vessel ID", min_value=1, step=1)
            vtype = st.text_input("Violation Type")
            details = st.text_area("Details")
            submitted = st.form_submit_button("Report Violation")
            if submitted:
                v = Violation(vessel_id, vtype, details)
                res = service.report_violation(v)
                if res.data:
                    st.success("Violation reported!")
                else:
                    st.error("Failed to report violation.")

    elif action == "Delete":
        violations = service.list_violations()
        df = pd.DataFrame(violations)
        if not df.empty:
            violation_id = st.selectbox("Select Violation ID", df["violation_id"])
            if st.button("Delete Violation"):
                res = service.dao.delete(violation_id)
                if res.data:
                    st.success("Violation deleted!")
                else:
                    st.error("Failed to delete violation.")

    st.subheader("Violations List")
    st.dataframe(pd.DataFrame(service.list_violations()))


# ==========================================================
# Staff Page
# ==========================================================
if page == "Staff":
    st.header("Staff")
    action = st.selectbox("Choose Action", ["View All", "Add", "Update", "Delete"])
    service = StaffService()

    if action == "Add":
        with st.form("add_staff"):
            name = st.text_input("Name")
            role = st.text_input("Role")
            contact = st.text_input("Contact Info")
            submitted = st.form_submit_button("Add Staff")
            if submitted:
                s = Staff(name, role, contact)
                res = service.add_staff(s)
                if res.data:
                    st.success("Staff added!")
                else:
                    st.error("Failed to add staff.")

    elif action == "Update":
        staff_list = service.list_staff()
        df = pd.DataFrame(staff_list)
        if not df.empty:
            staff_id = st.selectbox("Select Staff ID", df["staff_id"])
            name = st.text_input("Name")
            role = st.text_input("Role")
            contact = st.text_input("Contact Info")
            if st.button("Update Staff"):
                res = service.dao.update(staff_id, {
                    "name": name,
                    "role": role,
                    "contact_info": contact
                })
                if res.data:
                    st.success("Staff updated!")
                else:
                    st.error("Failed to update staff.")

    elif action == "Delete":
        staff_list = service.list_staff()
        df = pd.DataFrame(staff_list)
        if not df.empty:
            staff_id = st.selectbox("Select Staff ID", df["staff_id"])
            if st.button("Delete Staff"):
                res = service.dao.delete(staff_id)
                if res.data:
                    st.success("Staff deleted!")
                else:
                    st.error("Failed to delete staff.")

    st.subheader("Staff List")
    st.dataframe(pd.DataFrame(service.list_staff()))


# ==========================================================
# Dashboard Page
# ==========================================================
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
