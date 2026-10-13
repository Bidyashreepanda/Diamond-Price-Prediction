import streamlit as st
import pandas as pd
import pickle

# Page configuration
st.set_page_config(
    page_title="Diamond Price Prediction",
    page_icon="💎",
    layout="centered"
)

# App title
st.title("💎 Diamond Price Prediction")
st.write("Predict the price of a diamond using Machine Learning (KNN).")

# Load the trained model
@st.cache_resource
def load_model():
    with open("diamond_price_prediction_model.pkl", "rb") as file:
        return pickle.load(file)

try:
    model = load_model()
except Exception as e:
    st.error(f"Could not load the model: {e}")
    st.stop()

# User inputs
st.header("Enter Diamond Details")

carat = st.number_input(
    "Carat",
    min_value=0.1,
    max_value=5.0,
    value=1.0,
    step=0.1
)

cut = st.selectbox(
    "Cut",
    ["Fair", "Good", "Very Good", "Premium", "Ideal"]
)

color = st.selectbox(
    "Color",
    ["D", "E", "F", "G", "H", "I", "J"]
)

clarity = st.selectbox(
    "Clarity",
    ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
)

depth = st.number_input(
    "Depth (%)",
    min_value=40.0,
    max_value=80.0,
    value=61.5,
    step=0.1
)

table = st.number_input(
    "Table (%)",
    min_value=40.0,
    max_value=80.0,
    value=57.0,
    step=0.1
)

x = st.number_input(
    "Length (mm)",
    min_value=0.1,
    max_value=15.0,
    value=6.0,
    step=0.1
)

y = st.number_input(
    "Width (mm)",
    min_value=0.1,
    max_value=15.0,
    value=6.0,
    step=0.1
)

z = st.number_input(
    "Depth (mm)",
    min_value=0.1,
    max_value=10.0,
    value=3.7,
    step=0.1
)

# Prediction button
if st.button("Predict Diamond Price", type="primary"):
    input_data = pd.DataFrame([{
        "carat": carat,
        "cut": cut,
        "color": color,
        "clarity": clarity,
        "depth": depth,
        "table": table,
        "x": x,
        "y": y,
        "z": z
    }])

    try:
        prediction = model.predict(input_data)
        st.success(
            f"💰 Predicted Diamond Price: ${prediction[0]:,.2f}"
        )
    except Exception as e:
        st.error(f"Prediction failed: {e}")
        st.info(
            "Check that the input column names and preprocessing "
            "match the model used during training."
        )
