#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module uses pandasai and streamlit to produce a web-based app with data
visualizations for a brain artery network dataset
"""
import os

import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)

secret_values = os.environ['OPENAI_API_KEY'] #use the command 'export OPENAI_API_KEY={your API key}' 
llm = OpenAI(api_token=secret_values)

df = pd.read_excel('/Users/davidprendez/SoftwareDev/sample_data/Combined_CROP-BRAVE-IPH_DemoClin.xlsx')

smart_df = SmartDataframe(df, config={"llm": llm,"enable_cache": False,"save_charts": False,},)

def ai_viz():
    """
    Produces the text input for the pandasai feature of the app. Users enter their
    prompt directly and then pandasai uploads the corresponding visualization.

    """
    
    st.title("Hi, I'm BAVA AI! How can I help you today?")
   
    with st.form("Question"):
        question = st.text_input("Message BAVA AI below. For example, type 'Plot the average SBP across different age groups'.", value="", type="default")
        question_sent = st.form_submit_button("Send")
        if question_sent:
            with st.spinner():
                ai_output = smart_df.chat(question)

                if ai_output is not None:
                    st.write(str(ai_output))
                else:
                    st.write("Data visualization shared!")

def home_page():
    """
    Sample function for adding extra pages.
    """
    st.title("Brain Artery Visualization and Analysis")
    st.write("Software and App Development")

    button1 = st.button("3D Visualization")
    button2 = st.button("BAVA AI")

def main():
    """
    Creates a sidebar for navigating through pages and organizes the pages.
    """
    st.sidebar.title("Pages")
    selected_page = st.sidebar.radio("Select a page:", ("Home", "BAVA AI"))

    if selected_page == "Home":
        home_page()
        
    elif selected_page == "BAVA AI":
        ai_viz()

# Run the Streamlit app
if __name__ == "__main__":
    main()
    

