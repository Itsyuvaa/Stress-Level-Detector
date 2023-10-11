"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Stress Level Detector")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            "Unlock the power of stress detection with cutting-edge web development! Our platform utilizes advanced machine learning algorithm to analyze real-time data collected from smartwatches, providing you with invaluable insights into your stress levels. Say goodbye to stress-related uncertainty and hello to a happier, healthier you. Experience the future of stress management with our innovative web solution."  
    """, unsafe_allow_html=True)
