import streamlit as st
import pandas as pd

insights = pd.read_csv(
    "reports/business_insights.csv"
)

st.title(
    "📋 Business Insights"
)

st.success(
"""
Individuals with higher education
have significantly greater
probability of earning >50K.
"""
)

st.success(
"""
Capital gain is one of the strongest
income indicators.
"""
)

st.success(
"""
Married-civ-spouse category
shows highest income rates.
"""
)

st.dataframe(
    insights.head(20)
)