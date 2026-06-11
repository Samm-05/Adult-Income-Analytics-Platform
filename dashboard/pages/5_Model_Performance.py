import streamlit as st
import pandas as pd
import plotly.express as px

results = pd.read_csv(
    "reports/model_comparison.csv"
)

st.title("🤖 Model Performance")

st.dataframe(
    results
)

fig = px.bar(
    results,
    x="Model",
    y="Accuracy"
)

st.plotly_chart(
    fig,
    use_container_width=True
)