
import streamlit as st
import pandas as pd
from supabase import create_client

# SERVICES
from src.services.owners_service import OwnersService
from src.services.vessels_service import VesselsService
from src.services.dockings_service import DockingsService
from src.services.payments_service import PaymentsService
from src.services.violations_service import ViolationsService
from src.services.staff_service import StaffService

# MODELS
from src.models.owner import Owner
from src.models.vessel import Vessel
from src.models.docking import Docking
from src.models.payment import Payment
from src.models.violation import Violation
from src.models.staff import Staff

# DASHBOARD
from src.dashboard.dashboard import Dashboard

# ---------- SUPABASE INIT ----------
url = st.secrets["supabase"]["url"]
key = st.secrets["supabase"]["key"]
supabase = create_client(url, key)

# ---------- SESSION STATE ----------
if "user" not in st.session_state:
    st.session_state.user = None

def logout():
    st.session_state.user = None
    st.query_params.clear()
    st.experimental_rerun()

def login():
    st.markdown("""
        <style>
        .login-card {
            max-width: 400px;
            margin: 5% auto;
            padding: 30px;
            background: white;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
            text-align: center;
            font-family: 'Arial', sans-serif;
        }
        .login-title {
            font-size: 24px;
            font-weight: bold;
            color: #006D77;
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #006D77;
            color: white;
            border-radius: 8px;
            font-weight: bold;
            width: 100%;
        }
        .stTextInput>div>div>input {
            border-radius: 8px;
            border: 1px solid #006D77;
            padding: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown('<div class="login-title">🔐 Staff Login</div>', unsafe_allow_html=True)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            res = supabase.auth.sign_in_with_password({"email": email, "password": password})
            if res.user:
                st.session_state.user = res.user.email
                st.success("✅ Login successful")
                st.experimental_rerun()
            else:
                st.error("❌ Invalid credentials")
        except Exception as e:
            st.error(f"Login failed: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

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

# ---------- HEADER ----------
st.markdown('<div class="main-header">MARINA MANAGEMENT SYSTEM 🚤</div>', unsafe_allow_html=True)

# ---------- SIDEBAR ----------
protected_pages = ["Owners", "Vessels", "Dockings", "Payments", "Violations", "Staff"]
page = st.sidebar.selectbox("Menu", ["Dashboard"] + protected_pages)

# ---------- LOGIN CHECK ----------
if page in protected_pages and not st.session_state.user:
    login()
    st.stop()

if st.session_state.user:
    st.sidebar.success(f"👤 Logged in as: {st.session_state.user}")
    if st.sidebar.button("Logout"):
        logout()

# ---------- DASHBOARD ----------
if page == "Dashboard":
    st.header("📊 Marina Dashboard")
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
    st.subheader("🌍 Vessel Activity Map")
    try:
        vessel_map = dashboard.vessel_map()
        if vessel_map:
            st.plotly_chart(vessel_map, use_container_width=True)
    except Exception as e:
        st.error(f"Error loading map: {e}")

# ========== REUSABLE CRUD PAGES ==========
from src.ui_pages.owners_page import render_owners_page
from src.ui_pages.vessels_page import render_vessels_page
from src.ui_pages.dockings_page import render_dockings_page
from src.ui_pages.payments_page import render_payments_page
from src.ui_pages.violations_page import render_violations_page
from src.ui_pages.staff_page import render_staff_page

if page == "Owners":
    render_owners_page()

elif page == "Vessels":
    render_vessels_page()

elif page == "Dockings":
    render_dockings_page()

elif page == "Payments":
    render_payments_page()

elif page == "Violations":
    render_violations_page()

elif page == "Staff":
    render_staff_page()

