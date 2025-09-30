'''import streamlit as st
from src.services.owner_service import OwnerService
from src.services.vessel_service import VesselService
from src.services.docking_service import DockingService
from src.services.payment_service import PaymentService
from src.services.violation_service import ViolationService
from src.services.staff_service import StaffService

# ------------------------------
# Initialize services
# ------------------------------
owner_service = OwnerService()
vessel_service = VesselService()
docking_service = DockingService()
payment_service = PaymentService()
violation_service = ViolationService()
staff_service = StaffService()

# ------------------------------
# App Layout
# ------------------------------
st.set_page_config(page_title="Marina Management System", layout="wide")
st.title("Marina Management System")

menu = ["Home", "Owners", "Vessels", "Dockings", "Payments", "Violations", "Staff"]
choice = st.sidebar.selectbox("Select Module", menu)

# ------------------------------
# Home Page
# ------------------------------
if choice == "Home":
    st.subheader("Welcome to the Marina Management System")
    st.write("Use the sidebar to navigate to different modules.")

# ------------------------------
# Owners
# ------------------------------
elif choice == "Owners":
    st.subheader("Manage Owners")
    owners = owner_service.get_all_owners()
    st.table(owners)

    st.write("### Add New Owner")
    name = st.text_input("Name")
    email = st.text_input("Email")
    if st.button("Add Owner"):
        owner_service.add_owner(name, email)
        st.success("Owner added successfully!")
        st.experimental_rerun()

# ------------------------------
# Vessels
# ------------------------------
elif choice == "Vessels":
    st.subheader("Manage Vessels")
    vessels = vessel_service.get_all_vessels()
    st.table(vessels)

# ------------------------------
# Dockings
# ------------------------------
elif choice == "Dockings":
    st.subheader("Manage Dockings")
    dockings = docking_service.get_all_dockings()
    st.table(dockings)

# ------------------------------
# Payments
# ------------------------------
elif choice == "Payments":
    st.subheader("Manage Payments")
    payments = payment_service.get_all_payments()
    st.table(payments)

# ------------------------------
# Violations
# ------------------------------
elif choice == "Violations":
    st.subheader("Manage Violations")
    violations = violation_service.get_all_violations()
    st.table(violations)

# ------------------------------
# Staff
# ------------------------------
elif choice == "Staff":
    st.subheader("Manage Staff")
    staff = staff_service.get_all_staff()
    st.table(staff)
'''
# app.py
import streamlit as st
import pandas as pd

from src.services.owner_service import OwnerService
from src.services.vessel_service import VesselService
from src.services.docking_service import DockingService
from src.services.payment_service import PaymentService
from src.services.violation_service import ViolationService
from src.services.staff_service import StaffService

st.set_page_config(page_title="Marina Management System", layout="wide")

owner_service = OwnerService()
vessel_service = VesselService()
docking_service = DockingService()
payment_service = PaymentService()
violation_service = ViolationService()
staff_service = StaffService()

menu = ["Home", "Owners", "Vessels", "Dockings", "Payments", "Violations", "Staff"]
choice = st.sidebar.selectbox("Select Module", menu)

if choice == "Home":
    st.title("Marina Management System")
    st.write("Use the sidebar to navigate to different modules.")

# --------------------- Owners ---------------------
elif choice == "Owners":
    st.title("Owners")
    owners = owner_service.get_all_owners()
    if owners:
        st.dataframe(pd.DataFrame(owners))
    else:
        st.info("No owners found.")

    st.header("Add Owner")
    with st.form("add_owner_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        submitted = st.form_submit_button("Add Owner")
    if submitted:
        if not name or not email:
            st.error("Provide both name and email.")
        else:
            try:
                row = owner_service.add_owner(name, email)
                st.success(f"Owner '{name}' added.")
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Error adding owner: {e}")

# --------------------- Vessels ---------------------
elif choice == "Vessels":
    st.title("Vessels")
    vessels = vessel_service.get_all_vessels()
    if vessels:
        st.dataframe(pd.DataFrame(vessels))
    else:
        st.info("No vessels found.")

    st.header("Add Vessel")
    with st.form("add_vessel_form"):
        name = st.text_input("Vessel Name")
        vessel_type = st.text_input("Vessel Type")
        owner_id = st.number_input("Owner ID", min_value=1, step=1)
        submitted = st.form_submit_button("Add Vessel")
    if submitted:
        if not name or not vessel_type:
            st.error("Fill vessel name and type.")
        else:
            try:
                vessel_service.add_vessel(name, vessel_type, owner_id)
                st.success("Vessel added.")
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Error adding vessel: {e}")

# --------------------- Dockings ---------------------
elif choice == "Dockings":
    st.title("Dockings")
    dockings = docking_service.get_all_dockings()
    if dockings:
        st.dataframe(pd.DataFrame(dockings))
    else:
        st.info("No dockings found.")

    st.header("Add Docking")
    with st.form("add_docking_form"):
        vessel_id = st.number_input("Vessel ID", min_value=1, step=1)
        dock_number = st.text_input("Dock Number")
        duration = st.number_input("Duration (hours)", min_value=1, step=1)
        submitted = st.form_submit_button("Add Docking")
    if submitted:
        if not dock_number:
            st.error("Provide a dock number.")
        else:
            try:
                docking_service.add_docking(vessel_id, dock_number, duration)
                st.success("Docking added.")
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Error adding docking: {e}")

# --------------------- Payments ---------------------
elif choice == "Payments":
    st.title("Payments")
    payments = payment_service.get_all_payments()
    if payments:
        st.dataframe(pd.DataFrame(payments))
    else:
        st.info("No payments found.")

    st.header("Add Payment")
    with st.form("add_payment_form"):
        owner_id = st.number_input("Owner ID", min_value=1, step=1)
        amount = st.number_input("Amount", min_value=0.0, step=0.1)
        status = st.selectbox("Status", ["Pending", "Completed"])
        submitted = st.form_submit_button("Add Payment")
    if submitted:
        if amount <= 0:
            st.error("Enter a valid amount.")
        else:
            try:
                payment_service.add_payment(owner_id, amount, status)
                st.success("Payment added.")
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Error adding payment: {e}")

# --------------------- Violations ---------------------
elif choice == "Violations":
    st.title("Violations")
    violations = violation_service.get_all_violations()
    if violations:
        st.dataframe(pd.DataFrame(violations))
    else:
        st.info("No violations found.")

    st.header("Add Violation")
    with st.form("add_violation_form"):
        vessel_id = st.number_input("Vessel ID", min_value=1, step=1)
        description = st.text_area("Description")
        fine = st.number_input("Fine Amount", min_value=0.0, step=0.1)
        submitted = st.form_submit_button("Add Violation")
    if submitted:
        if not description:
            st.error("Describe the violation.")
        else:
            try:
                violation_service.add_violation(vessel_id, description, fine)
                st.success("Violation recorded.")
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Error adding violation: {e}")

# --------------------- Staff ---------------------
elif choice == "Staff":
    st.title("Staff")
    staff = staff_service.get_all_staff()
    if staff:
        st.dataframe(pd.DataFrame(staff))
    else:
        st.info("No staff found.")

    st.header("Add Staff")
    with st.form("add_staff_form"):
        name = st.text_input("Staff Name")
        role = st.text_input("Role")
        submitted = st.form_submit_button("Add Staff")
    if submitted:
        if not name or not role:
            st.error("Provide name and role.")
        else:
            try:
                staff_service.add_staff(name, role)
                st.success("Staff added.")
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Error adding staff: {e}")
