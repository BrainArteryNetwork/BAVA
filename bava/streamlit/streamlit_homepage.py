import streamlit as st
from bava.streamlit.streamlit_pandasai import page_pandasai
from bava.streamlit.streamlit_visualization3d import page_viz3d

def home_page():
    """
    Sample function for adding extra pages.
    """
    st.title("Brain Artery Visualization and Analysis")
    # st.write("Software and App Development")

    button1 = st.button("3D Visualization")
    button2 = st.button("BAVA AI")

    if button1:
        page_viz3d()  # Call the page_viz3d function when button1 is clicked

    if button2:
        page_pandasai()  # Call the page_pandasai function when button2 is clicked

if __name__ == "__main__":
    home_page()