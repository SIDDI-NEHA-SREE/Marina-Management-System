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

# ================= OWNERS =================
if page == "Owners":
    st.header("Owners")
    choice = st.radio("Action", ["Add", "Update", "Delete", "View"])
    service = OwnersService()

    if choice == "Add":
        with st.form("owner_form"):
            name = st.text_input("Name")
            address = st.text_input("Address")
            phone = st.text_input("Phone")
            email = st.text_input("Email")
            submitted = st.form_submit_button("Add Owner")
            if submitted:
                o = Owner(name, address, phone, email)
                service.create_owner(o)
                st.success("Owner added!")

    elif choice == "Update":
        owners = service.list_owners()
        df = pd.DataFrame(owners)
        if not df.empty:
            selected = st.selectbox("Select Owner to Update", df["owner_id"])
            with st.form("update_owner"):
                name = st.text_input("Name", df.loc[df["owner_id"]==selected,"name"].values[0])
                address = st.text_input("Address", df.loc[df["owner_id"]==selected,"address"].values[0])
                phone = st.text_input("Phone", df.loc[df["owner_id"]==selected,"phone"].values[0])
                email = st.text_input("Email", df.loc[df["owner_id"]==selected,"email"].values[0])
                submitted = st.form_submit_button("Update")
                if submitted:
                    service.dao.update(selected, {
                        "name": name, "address": address, "phone": phone, "email": email
                    }, id_field="owner_id")
                    st.success("Owner updated!")

    elif choice == "Delete":
        owners = service.list_owners()
        df = pd.DataFrame(owners)
        if not df.empty:
            selected = st.selectbox("Select Owner to Delete", df["owner_id"])
            if st.button("Delete"):
                service.dao.delete(selected, id_field="owner_id")
                st.success("Owner deleted!")

    st.subheader("Owners List")
    st.dataframe(pd.DataFrame(service.list_owners()))

# ================= VESSELS =================
if page == "Vessels":
    st.header("Vessels")
    choice = st.radio("Action", ["Add", "Update", "Delete", "View"])
    service = VesselsService()

    if choice == "Add":
        with st.form("vessel_form"):
            vessel_name = st.text_input("Vessel Name")
            vessel_type = st.text_input("Vessel Type")
            capacity = st.number_input("Capacity", min_value=0)
            owner_id = st.number_input("Owner ID", min_value=1)
            reg = st.text_input("Registration Number")
            submitted = st.form_submit_button("Add Vessel")
            if submitted:
                v = Vessel(vessel_name, vessel_type, capacity, owner_id, reg)
                service.create_vessel(v)
                st.success("Vessel added!")

    elif choice == "Update":
        vessels = service.list_vessels()
        df = pd.DataFrame(vessels)
        if not df.empty:
            selected = st.selectbox("Select Vessel", df["vessel_id"])
            with st.form("update_vessel"):
                vessel_name = st.text_input("Name", df.loc[df["vessel_id"]==selected,"vessel_name"].values[0])
                vessel_type = st.text_input("Type", df.loc[df["vessel_id"]==selected,"vessel_type"].values[0])
                submitted = st.form_submit_button("Update")
                if submitted:
                    service.dao.update(selected, {"vessel_name": vessel_name, "vessel_type": vessel_type}, id_field="vessel_id")
                    st.success("Vessel updated!")

    elif choice == "Delete":
        vessels = service.list_vessels()
        df = pd.DataFrame(vessels)
        if not df.empty:
            selected = st.selectbox("Select Vessel to Delete", df["vessel_id"])
            if st.button("Delete"):
                service.dao.delete(selected, id_field="vessel_id")
                st.success("Vessel deleted!")

    st.subheader("Vessels List")
    st.dataframe(pd.DataFrame(service.list_vessels()))

# ================= DOCKINGS =================
if page == "Dockings":
    st.header("Dockings")
    choice = st.radio("Action", ["Add", "Update", "Delete", "View"])
    service = DockingsService()

    if choice == "Add":
        with st.form("dock_form"):
            vessel_id = st.number_input("Vessel ID", min_value=1)
            dock_location = st.text_input("Dock Location")
            dock_capacity = st.number_input("Capacity", min_value=1)
            submitted = st.form_submit_button("Dock Vessel")
            if submitted:
                d = Docking(vessel_id, dock_location, dock_capacity)
                service.dock_vessel(d)
                st.success("Docking recorded!")

    elif choice == "Update":
        dockings = service.list_dockings()
        df = pd.DataFrame(dockings)
        if not df.empty:
            selected = st.selectbox("Select Docking", df["docking_id"])
            with st.form("update_docking"):
                dock_location = st.text_input("Dock Location", df.loc[df["docking_id"]==selected,"dock_location"].values[0])
                status = st.text_input("Status", df.loc[df["docking_id"]==selected,"status"].values[0])
                submitted = st.form_submit_button("Update")
                if submitted:
                    service.dao.update(selected, {"dock_location": dock_location, "status": status}, id_field="docking_id")
                    st.success("Docking updated!")

    elif choice == "Delete":
        dockings = service.list_dockings()
        df = pd.DataFrame(dockings)
        if not df.empty:
            selected = st.selectbox("Select Docking to Delete", df["docking_id"])
            if st.button("Delete"):
                service.dao.delete(selected, id_field="docking_id")
                st.success("Docking deleted!")

    st.subheader("Dockings List")
    st.dataframe(pd.DataFrame(service.list_dockings()))

# ================= PAYMENTS =================
if page == "Payments":
    st.header("Payments")
    choice = st.radio("Action", ["Add", "Update", "Delete", "View"])
    service = PaymentsService()

    if choice == "Add":
        with st.form("payment_form"):
            vessel_id = st.number_input("Vessel ID", min_value=1)
            amount = st.number_input("Amount", min_value=0.0)
            payment_type = st.text_input("Payment Type")
            tax = st.number_input("Tax", min_value=0.0)
            submitted = st.form_submit_button("Record Payment")
            if submitted:
                p = Payment(vessel_id, amount, payment_type, tax)
                service.record_payment(p)
                st.success("Payment recorded!")

    elif choice == "Update":
        payments = service.list_payments()
        df = pd.DataFrame(payments)
        if not df.empty:
            selected = st.selectbox("Select Payment", df["payment_id"])
            with st.form("update_payment"):
                amount = st.number_input("Amount", value=float(df.loc[df["payment_id"]==selected,"amount"].values[0]))
                payment_type = st.text_input("Payment Type", df.loc[df["payment_id"]==selected,"payment_type"].values[0])
                submitted = st.form_submit_button("Update")
                if submitted:
                    service.dao.update(selected, {"amount": amount, "payment_type": payment_type}, id_field="payment_id")
                    st.success("Payment updated!")

    elif choice == "Delete":
        payments = service.list_payments()
        df = pd.DataFrame(payments)
        if not df.empty:
            selected = st.selectbox("Select Payment to Delete", df["payment_id"])
            if st.button("Delete"):
                service.dao.delete(selected, id_field="payment_id")
                st.success("Payment deleted!")

    st.subheader("Payments List")
    st.dataframe(pd.DataFrame(service.list_payments()))

# ================= VIOLATIONS =================
if page == "Violations":
    st.header("Violations")
    choice = st.radio("Action", ["Add", "Update", "Delete", "View"])
    service = ViolationsService()

    if choice == "Add":
        with st.form("violation_form"):
            vessel_id = st.number_input("Vessel ID", min_value=1)
            vtype = st.text_input("Violation Type")
            details = st.text_area("Details")
            submitted = st.form_submit_button("Report Violation")
            if submitted:
                v = Violation(vessel_id, vtype, details)
                service.report_violation(v)
                st.success("Violation reported!")

    elif choice == "Update":
        violations = service.list_violations()
        df = pd.DataFrame(violations)
        if not df.empty:
            selected = st.selectbox("Select Violation", df["violation_id"])
            with st.form("update_violation"):
                vtype = st.text_input("Violation Type", df.loc[df["violation_id"]==selected,"violation_type"].values[0])
                details = st.text_area("Details", df.loc[df["violation_id"]==selected,"details"].values[0])
                submitted = st.form_submit_button("Update")
                if submitted:
                    service.dao.update(selected, {"violation_type": vtype, "details": details}, id_field="violation_id")
                    st.success("Violation updated!")

    elif choice == "Delete":
        violations = service.list_violations()
        df = pd.DataFrame(violations)
        if not df.empty:
            selected = st.selectbox("Select Violation to Delete", df["violation_id"])
            if st.button("Delete"):
                service.dao.delete(selected, id_field="violation_id")
                st.success("Violation deleted!")

    st.subheader("Violations List")
    st.dataframe(pd.DataFrame(service.list_violations()))

# ================= STAFF =================
if page == "Staff":
    st.header("Staff")
    choice = st.radio("Action", ["Add", "Update", "Delete", "View"])
    service = StaffService()

    if choice == "Add":
        with st.form("staff_form"):
            name = st.text_input("Name")
            role = st.text_input("Role")
            contact = st.text_input("Contact Info")
            submitted = st.form_submit_button("Add Staff")
            if submitted:
                s = Staff(name, role, contact)
                service.add_staff(s)
                st.success("Staff added!")

    elif choice == "Update":
        staff_list = service.list_staff()
        df = pd.DataFrame(staff_list)
        if not df.empty:
            selected = st.selectbox("Select Staff", df["staff_id"])
            with st.form("update_staff"):
                name = st.text_input("Name", df.loc[df["staff_id"]==selected,"name"].values[0])
                role = st.text_input("Role", df.loc[df["staff_id"]==selected,"role"].values[0])
                submitted = st.form_submit_button("Update")
                if submitted:
                    service.dao.update(selected, {"name": name, "role": role}, id_field="staff_id")
                    st.success("Staff updated!")

    elif choice == "Delete":
        staff_list = service.list_staff()
        df = pd.DataFrame(staff_list)
        if not df.empty:
            selected = st.selectbox("Select Staff to Delete", df["staff_id"])
            if st.button("Delete"):
                service.dao.delete(selected, id_field="staff_id")
                st.success("Staff deleted!")

    st.subheader("Staff List")
    st.dataframe(pd.DataFrame(service.list_staff()))

# ================= DASHBOARD =================
if page == "Dashboard":
    st.header("📊 Marina Dashboard")
    dashboard = Dashboard()

    col1, col2 = st.columns(2)
    with col1:
        fig1 = dashboard.vessel_type_distribution()
        if fig1:
            st.plotly_chart(fig1, use_container_width=True)
        else:
            st.info("No vessel data available.")

    with col2:
        fig2 = dashboard.dock_occupancy()
        if fig2:
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info("No docking data available.")

    col3, col4 = st.columns(2)
    with col3:
        fig3 = dashboard.revenue_over_time()
        if fig3:
            st.plotly_chart(fig3, use_container_width=True)
        else:
            st.info("No payment data available.")
    with col4:
        fig4 = dashboard.violations_by_type()
        if fig4:
            st.plotly_chart(fig4, use_container_width=True)
        else:
            st.info("No violation data available.")
