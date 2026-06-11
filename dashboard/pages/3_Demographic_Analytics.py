import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv(
    "data/processed/engineered_adult.csv"
)

st.title("🧑 Demographic Analytics")

if "sex_Male" in df.columns:

    gender = (
        df.groupby("sex_Male")
        ["income"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        gender,
        x="sex_Male",
        y="income"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )