import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from components.trending import render_trending_tab
from components.explorer import render_explorer_tab
from components.recommendations import render_recommendations_tab
from components.alerts import render_alerts_tab

st.set_page_config(page_title="VA Market Trend Dashboard", layout="wide")
st.title("Virtual Assistant Market Trend Co-Pilot")

# Sidebar navigation
tabs = ["Trending Products", "Product Explorer", "Recommendations", "Alerts"]
selected_tab = st.sidebar.radio("Navigation", tabs)

# Route to tab content
if selected_tab == "Trending Products":
    render_trending_tab()
elif selected_tab == "Product Explorer":
    render_explorer_tab()
elif selected_tab == "Recommendations":
    render_recommendations_tab()
elif selected_tab == "Alerts":
    render_alerts_tab()
