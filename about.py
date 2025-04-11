import streamlit as st
import pandas as pd
from PIL import Image

def app():
    # st.markdown("# About Us")
    logo = Image.open('Assets/HYTRA logo.png')
    charts = Image.open('Assets/Landing Plots 2.png')

    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("# About Us", unsafe_allow_html=True)
    with col2:
        st.image(logo, width=250)
    st.markdown("## WELCOME TO RECURA: ONE HEALTH DASHBOARD")
    st.markdown("### We are here for all your diagnostics")
    st.markdown(
        """<div style='text-align: justify;'>
        Stay on top of your health with ReCura, offering comprehensive insights that most other dashboards can't provide. Sign up today and take control of your health journey. ReCura is designed to empower you with data-driven decisions, helping you understand your health metrics in a clear and actionable way. Our platform goes beyond mere numbers; it transforms data into meaningful narratives about your health. From tracking heart rate to predicting readmission risks, ReCura covers every aspect of your well-being, providing personalized insights that make a real difference. With features that allow you to monitor your progress over time, set health goals, and receive tailored recommendations, you can make informed choices that enhance your quality of life. Join us now to experience a new era of health management that is proactive, precise, and perfectly tailored to your needs. Together, we can build a healthier future, one informed decision at a time. Your health is our priority, and we are committed to supporting you every step of the way.
        </div><br />""",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(charts, width=500)
        st.markdown("One stop for your all key health metrics.")

    st.markdown("---")
    st.markdown("## Why ReCura is the best option?")

    features = [
        "Heart Rate", "Blood Pressure", "Body Weight", "Steps", "Body Fat", "Sleep Time", "Health Level Percent", "Readmission Risk"
    ]

    hytra_features = ["\u2714"] * 8
    other_dashboards = ["\u2714", "\u2714", "\u2714", "\u2714", "\u2714", "\u2714", "\u274c", "\u274c"]

    comparison_data = pd.DataFrame({
        "Features": features,
        "ReCura": hytra_features,
        "Others": other_dashboards
    }).reset_index(drop=True)

    st.markdown(
        """
        <style>
        /* Center the table on the page */
        [data-testid="stTable"] table {
            margin-left: auto;
            margin-right: auto;
        }

        /* Style all table headers and cells */
        [data-testid="stTable"] th, [data-testid="stTable"] td {
            padding: 10px !important;
            text-align: center !important;
            white-space: pre-wrap !important; /* or normal */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display using st.table
    st.table(comparison_data)

    st.markdown(
        """
        <style>
        .stButton > button {
            background-color: #4901c5;
            color: white;
            font-size: 16px;
            padding: 10px 24px;
        }
        .stTable {
            font-size: 18px;
        }
        .hover-button:hover {
            background-color: white;
            color: #4901c5;
            border: 2px solid #4901c5;
        }
        </style>
        """,
        unsafe_allow_html=True
    )