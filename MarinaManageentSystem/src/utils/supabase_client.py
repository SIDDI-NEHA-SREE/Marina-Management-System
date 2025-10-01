from supabase import create_client
import streamlit as st

# Read Supabase credentials from Streamlit secrets
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

# Create the Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
