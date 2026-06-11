import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv(
    "data/processed/engineered_adult.csv"
)

st.title("📊 Income Analytics")

fig = px.histogram(
    df,
    x="age",
    color="income",
    title="Age vs Income"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig2 = px.histogram(
    df,
    x="hours.per.week",
    color="income"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)