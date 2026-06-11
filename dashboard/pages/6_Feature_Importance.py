import streamlit as st
import pandas as pd
import plotly.express as px

importance = pd.read_csv(
    "reports/feature_importance.csv"
)

st.title(
    "📈 Feature Importance"
)

fig = px.bar(
    importance.head(20),
    x="Importance",
    y="Feature",
    orientation="h"
)

st.plotly_chart(
    fig,
    use_container_width=True
)