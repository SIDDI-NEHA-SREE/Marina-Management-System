from supabase import create_client
import streamlit as st

# Get secrets from Streamlit (set in .streamlit/secrets.toml)
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

# Global Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
