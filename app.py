import streamlit as st
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
