import streamlit as st
import pandas as pd
import joblib

model = joblib.load(
    "models/best_model.pkl"
)

scaler = joblib.load(
    "models/scaler.pkl"
)

features = joblib.load(
    "models/feature_names.pkl"
)

st.title("💰 Income Predictor")

age = st.slider(
    "Age",
    18,
    80,
    35
)

education_num = st.slider(
    "Education Years",
    1,
    16,
    10
)

hours = st.slider(
    "Hours Per Week",
    1,
    100,
    40
)

capital_gain = st.number_input(
    "Capital Gain",
    0
)

capital_loss = st.number_input(
    "Capital Loss",
    0
)

if st.button(
    "Predict Income"
):

    row = {
        feature:0
        for feature in features
    }

    if "age" in row:
        row["age"] = age

    if "education.num" in row:
        row["education.num"] = education_num

    if "hours.per.week" in row:
        row["hours.per.week"] = hours

    if "capital.gain" in row:
        row["capital.gain"] = capital_gain

    if "capital.loss" in row:
        row["capital.loss"] = capital_loss

    sample = pd.DataFrame(
        [row]
    )

    sample_scaled = scaler.transform(
        sample
    )

    prediction = model.predict(
        sample_scaled
    )[0]

    probability = model.predict_proba(
        sample_scaled
    )[0][1]

    if prediction == 1:

        st.success(
            f"Income >50K ({probability:.2%})"
        )

    else:

        st.error(
            f"Income <=50K ({1-probability:.2%})"
        )

    st.progress(
        int(probability*100)
    )