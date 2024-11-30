import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"


def month_analytics_tab():
    # Month and year selection
    col1, col2 = st.columns(2)
    with col1:
        month = st.selectbox("Select Month", list(range(1, 13)),
                             format_func=lambda x: datetime(2024, x, 1).strftime('%B'))
    with col2:
        year = st.number_input("Select Year", min_value=2000, max_value=datetime.now().year, value=2024, step=1)

    if st.button("Get Monthly Analytics"):
        payload = {
            "month": month,
            "year": year
        }

        # Make a POST request to the /analytics_by_month/ endpoint
        response = requests.post(f"{API_URL}/analytics_by_month/", json=payload)

        if response.status_code == 200:
            response = response.json()

            # Extract the total expense and breakdown from the response
            total_expense = response["total_expense"]
            breakdown = response["breakdown"]

            # Prepare data for display
            data = {
                "Category": list(breakdown.keys()),
                "Total": [breakdown[category]["total"] for category in breakdown],
                "Percentage": [breakdown[category]["percentage"] for category in breakdown]
            }

            df = pd.DataFrame(data)
            df_sorted = df.sort_values(by="Percentage", ascending=False)

            # Display total expense
            st.subheader(f"Total Expense for {datetime(2024, month, 1).strftime('%B')} {year}: ₹{total_expense:.2f}")

            # Display bar chart
            st.subheader("Expense Breakdown By Category")
            st.bar_chart(data=df_sorted.set_index("Category")['Percentage'], use_container_width=True)

            # Format total and percentage columns
            df_sorted["Total"] = df_sorted["Total"].map("₹{:.2f}".format)
            df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}%".format)

            # Display table
            st.table(df_sorted)

        else:
            st.error("Failed to retrieve data. Please check your API connection or input values.")
