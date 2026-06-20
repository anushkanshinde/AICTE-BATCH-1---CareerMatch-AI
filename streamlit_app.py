import streamlit as st
import requests

st.title("CareerMatch AI")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    files = {
        "file": uploaded_file
    }

    response = requests.post(
        "http://127.0.0.1:8000/analyze",
        files=files
    )

    result = response.json()

    st.success(
        result["career_prediction"]
    )

    st.write(
        "Detected Skills"
    )

    st.write(
        result["detected_skills"]
    )

    st.write(
        "Missing Skills"
    )

    st.write(
        result["missing_skills"]
    )

    st.write(
        result["career_advice"]
    )