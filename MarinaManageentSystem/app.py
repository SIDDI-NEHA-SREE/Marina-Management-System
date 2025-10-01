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


# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Marina Management System", layout="wide")

# ---------- GLOBAL CSS ----------
st.markdown("""
    <style>
    body { background-color: #f6fbfc; }
    .main-header {
        background-color: #006D77;
        color: white;
        text-align: center;
        padding: 15px;
        font-size: 30px;
        font-weight: bold;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .section-header {
        color: #006D77;
        font-size: 22px;
        margin-top: 20px;
        font-weight: bold;
    }
    .form-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)


# ---------- APP HEADER ----------
st.markdown('<div class="main-header">MARINA MANAGEMENT SYSTEM 🚤</div>', unsafe_allow_html=True)

# Sidebar
page = st.sidebar.selectbox("Menu", [
    "Dashboard", "Owners", "Vessels", "Dockings", "Payments", "Violations", "Staff"
])


# ---------------- Owners ----------------
if page == "Owners":
    st.markdown('<div class="section-header">👤 Owners</div>', unsafe_allow_html=True)
    service = OwnersService()
    action = st.selectbox("Choose Action", ["Add", "Update", "Delete", "View"])

    if action == "Add":
        with st.form("add_owner", clear_on_submit=True):
            st.markdown('<div class="form-card">', unsafe_allow_html=True)
            name = st.text_input("Name")
            address = st.text_input("Address")
            phone = st.text_input("Phone")
            email = st.text_input("Email")
            submitted = st.form_submit_button("➕ Add Owner")
            if submitted:
                service.create_owner(Owner(name, address, phone, email))
                st.success("✅ Owner added successfully!")
            st.markdown('</div>', unsafe_allow_html=True)

    elif action == "Update":
        owners = service.list_owners()
        if owners:
            df = pd.DataFrame(owners)
            owner_id = st.selectbox("Select Owner ID", df["owner_id"])
            new_address = st.text_input("New Address")
            if st.button("✏️ Update Owner"):
                service.update_owner(owner_id, {"address": new_address})
                st.success("✅ Owner updated!")

    elif action == "Delete":
        owners = service.list_owners()
        if owners:
            df = pd.DataFrame(owners)
            owner_id = st.selectbox("Select Owner ID", df["owner_id"])
            if st.button("🗑️ Delete Owner"):
                service.delete_owner(owner_id)
                st.success("🗑️ Owner deleted!")

    elif action == "View":
        st.dataframe(pd.DataFrame(service.list_owners()))


# ---------------- Vessels ----------------
if page == "Vessels":
    st.markdown('<div class="section-header">⛵ Vessels</div>', unsafe_allow_html=True)
    service = VesselsService()
    action = st.selectbox("Choose Action", ["Add", "Update", "Delete", "View"])

    if action == "Add":
        with st.form("add_vessel", clear_on_submit=True):
            st.markdown('<div class="form-card">', unsafe_allow_html=True)
            vessel_name = st.text_input("Vessel Name")
            vessel_type = st.text_input("Vessel Type")
            capacity = st.number_input("Capacity", min_value=0)
            owner_id = st.number_input("Owner ID", min_value=1)
            reg = st.text_input("Registration Number")
            submitted = st.form_submit_button("➕ Add Vessel")
            if submitted:
                service.create_vessel(Vessel(vessel_name, vessel_type, capacity, owner_id, reg))
                st.success("✅ Vessel added!")
            st.markdown('</div>', unsafe_allow_html=True)

    elif action == "Update":
        vessels = service.list_vessels()
        if vessels:
            df = pd.DataFrame(vessels)
            vessel_id = st.selectbox("Select Vessel ID", df["vessel_id"])
            new_type = st.text_input("New Vessel Type")
            if st.button("✏️ Update Vessel"):
                service.update_vessel(vessel_id, {"vessel_type": new_type})
                st.success("✅ Vessel updated!")

    elif action == "Delete":
        vessels = service.list_vessels()
        if vessels:
            df = pd.DataFrame(vessels)
            vessel_id = st.selectbox("Select Vessel ID", df["vessel_id"])
            if st.button("🗑️ Delete Vessel"):
                service.delete_vessel(vessel_id)
                st.success("🗑️ Vessel deleted!")

    elif action == "View":
        st.dataframe(pd.DataFrame(service.list_vessels()))


# ---------------- Dockings ----------------
if page == "Dockings":
    st.markdown('<div class="section-header">⚓ Dockings</div>', unsafe_allow_html=True)
    service = DockingsService()
    action = st.selectbox("Choose Action", ["Add", "Update", "Delete", "View"])

    if action == "Add":
        with st.form("add_docking", clear_on_submit=True):
            st.markdown('<div class="form-card">', unsafe_allow_html=True)
            vessel_id = st.number_input("Vessel ID", min_value=1)
            location = st.text_input("Dock Location")
            capacity = st.number_input("Dock Capacity", min_value=1)
            submitted = st.form_submit_button("➕ Add Docking")
            if submitted:
                service.dock_vessel(Docking(vessel_id, location, capacity))
                st.success("✅ Docking added!")
            st.markdown('</div>', unsafe_allow_html=True)

    elif action == "Update":
        dockings = service.list_dockings()
        if dockings:
            df = pd.DataFrame(dockings)
            docking_id = st.selectbox("Select Docking ID", df["docking_id"])
            new_status = st.text_input("New Status")
            if st.button("✏️ Update Docking"):
                service.update_docking(docking_id, {"status": new_status})
                st.success("✅ Docking updated!")

    elif action == "Delete":
        dockings = service.list_dockings()
        if dockings:
            df = pd.DataFrame(dockings)
            docking_id = st.selectbox("Select Docking ID", df["docking_id"])
            if st.button("🗑️ Delete Docking"):
                service.delete_docking(docking_id)
                st.success("🗑️ Docking deleted!")

    elif action == "View":
        st.dataframe(pd.DataFrame(service.list_dockings()))


# ---------------- Payments ----------------
if page == "Payments":
    st.markdown('<div class="section-header">💰 Payments</div>', unsafe_allow_html=True)
    service = PaymentsService()
    action = st.selectbox("Choose Action", ["Add", "View"])

    if action == "Add":
        with st.form("add_payment", clear_on_submit=True):
            st.markdown('<div class="form-card">', unsafe_allow_html=True)
            vessel_id = st.number_input("Vessel ID", min_value=1)
            amount = st.number_input("Amount", min_value=0.0)
            ptype = st.text_input("Payment Type")
            tax = st.number_input("Tax Amount", min_value=0.0)
            submitted = st.form_submit_button("➕ Record Payment")
            if submitted:
                service.record_payment(Payment(vessel_id, amount, ptype, tax))
                st.success("✅ Payment recorded!")
            st.markdown('</div>', unsafe_allow_html=True)

    elif action == "View":
        st.dataframe(pd.DataFrame(service.list_payments()))


# ---------------- Violations ----------------
if page == "Violations":
    st.markdown('<div class="section-header">🚨 Violations</div>', unsafe_allow_html=True)
    service = ViolationsService()
    action = st.selectbox("Choose Action", ["Add", "View"])

    if action == "Add":
        with st.form("add_violation", clear_on_submit=True):
            st.markdown('<div class="form-card">', unsafe_allow_html=True)
            vessel_id = st.number_input("Vessel ID", min_value=1)
            vtype = st.text_input("Violation Type")
            details = st.text_area("Details")
            submitted = st.form_submit_button("🚨 Report Violation")
            if submitted:
                service.report_violation(Violation(vessel_id, vtype, details))
                st.success("✅ Violation reported!")
            st.markdown('</div>', unsafe_allow_html=True)

    elif action == "View":
        st.dataframe(pd.DataFrame(service.list_violations()))


# ---------------- Staff ----------------
if page == "Staff":
    st.markdown('<div class="section-header">👨‍✈️ Staff</div>', unsafe_allow_html=True)
    service = StaffService()
    action = st.selectbox("Choose Action", ["Add", "Update", "Delete", "View"])

    if action == "Add":
        with st.form("add_staff", clear_on_submit=True):
            st.markdown('<div class="form-card">', unsafe_allow_html=True)
            name = st.text_input("Name")
            role = st.text_input("Role")
            contact = st.text_input("Contact Info")
            submitted = st.form_submit_button("➕ Add Staff")
            if submitted:
                service.add_staff(Staff(name, role, contact))
                st.success("✅ Staff added!")
            st.markdown('</div>', unsafe_allow_html=True)

    elif action == "Update":
        staff = service.list_staff()
        if staff:
            df = pd.DataFrame(staff)
            staff_id = st.selectbox("Select Staff ID", df["staff_id"])
            new_role = st.text_input("New Role")
            if st.button("✏️ Update Staff"):
                service.update_staff(staff_id, {"role": new_role})
                st.success("✅ Staff updated!")

    elif action == "Delete":
        staff = service.list_staff()
        if staff:
            df = pd.DataFrame(staff)
            staff_id = st.selectbox("Select Staff ID", df["staff_id"])
            if st.button("🗑️ Delete Staff"):
                service.delete_staff(staff_id)
                st.success("🗑️ Staff deleted!")

    elif action == "View":
        st.dataframe(pd.DataFrame(service.list_staff()))


# ---------------- Dashboard ----------------
if page == "Dashboard":
    from dashboard_ui import show_dashboard
    show_dashboard()
