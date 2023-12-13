"""
"""
import streamlit as st

def home_page():
    st.title("Brain Artery Network Visualization and Analysis (BAVA)")
    st.image("https://www.verywellhealth.com/thmb/ZCNl1MDrLcERy4vZJH5LKAH1qXA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/MiddleMeningealIllustration-f6adbace64e144d2aeb6760c4089594d.jpg")
    st.write("BAVA is a cutting-edge online platform designed for medical researchers focusing on neurology, particularly in the study of brain artery networks. It integrates powerful visualization tools with statistical analysis and artificial intelligence (AI) capabilities to facilitate the exploration and analysis of vascular diseases.")

if __name__ == "__main__":
    home_page()