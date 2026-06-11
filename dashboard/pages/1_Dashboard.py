import streamlit as st
import pandas as pd

df = pd.read_csv(
    "data/processed/engineered_adult.csv"
)

st.title("🏠 Executive Dashboard")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Total Records",
    len(df)
)

col2.metric(
    "High Income %",
    round(df["income"].mean()*100,2)
)

col3.metric(
    "Average Age",
    round(df["age"].mean(),1)
)

col4.metric(
    "Avg Hours/Week",
    round(df["hours.per.week"].mean(),1)
)

st.dataframe(
    df.head()
)