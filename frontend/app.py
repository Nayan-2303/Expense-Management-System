import streamlit as st
from add_update_ui import add_update_tab
from analytics_by_dates import analytics_tab
from analytics_by_month import month_analytics_tab


st.title("Expense Tracking System")

tab1, tab2, tab3= st.tabs(["Add/Update", "Analytics by Date", "Monthly Expense Analytics"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()

with tab3:
    month_analytics_tab()



