import streamlit as st
import plotly.express as px
import pandas as pd
from src.dashboard.dashboard import Dashboard

# Sea theme colors
SEA_COLORS = {
    "teal": "#006D77",
    "light_teal": "#83C5BE",
    "yellow": "#FFDD57",
    "orange": "#E29578",
    "red": "#B23A48"
}

def stat_card(title, value, color):
    """Reusable stat card component"""
    st.markdown(f"""
        <div style="
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
            text-align: center;
        ">
            <h4 style="color: {SEA_COLORS['teal']}; margin-bottom: 10px;">{title}</h4>
            <h2 style="color: {color}; font-weight: bold;">{value}</h2>
        </div>
    """, unsafe_allow_html=True)

def show_dashboard():
    dashboard = Dashboard()

    # ---------- TOP STATS ----------
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        stat_card("Berth Occupancy", "85%", SEA_COLORS["teal"])
    with col2:
        stat_card("Vessels Docked", "120", SEA_COLORS["light_teal"])
    with col3:
        stat_card("Pending Payments", "$15,000", SEA_COLORS["orange"])
    with col4:
        stat_card("Active Violations", "5", SEA_COLORS["red"])

    st.markdown("### 📊 Vessel Insights")

    # ---------- CHARTS ----------
    col5, col6 = st.columns(2)
    with col5:
        try:
            fig1 = dashboard.vessel_type_distribution()
            if fig1:
                st.plotly_chart(fig1, use_container_width=True)
        except Exception as e:
            st.error(f"Error loading chart: {e}")

    with col6:
        try:
            fig2 = dashboard.dock_occupancy()
            if fig2:
                st.plotly_chart(fig2, use_container_width=True)
        except Exception as e:
            st.error(f"Error loading chart: {e}")

    st.markdown("### 💰 Finance & Compliance")

    col7, col8 = st.columns(2)
    with col7:
        try:
            fig3 = dashboard.revenue_over_time()
            if fig3:
                st.plotly_chart(fig3, use_container_width=True)
        except Exception as e:
            st.error(f"Error loading chart: {e}")

    with col8:
        try:
            fig4 = dashboard.violations_by_type()
            if fig4:
                st.plotly_chart(fig4, use_container_width=True)
        except Exception as e:
            st.error(f"Error loading chart: {e}")
