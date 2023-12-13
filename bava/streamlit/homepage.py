"""
"""
import streamlit as st
from bava.streamlit.pandas_ai import page_pandasai
from bava.streamlit.data_visualization3d import page_viz3d

def home_page():
    st.title("Brain Artery Visualization and Analysis")

    # Hidden radio button to store the state
    state = st.radio("", ("Home", "Brain Network Visualization 3D", "BAVA AI"), index=0, key="hidden_state")

    if state == "Brain Network Visualization 3D":
        page_viz3d()

    if state == "BAVA AI":
        page_pandasai()

if __name__ == "__main__":
    home_page()