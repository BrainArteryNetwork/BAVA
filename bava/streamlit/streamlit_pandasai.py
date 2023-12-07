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

secret_values = os.environ['OPENAI_API_KEY'] # use 'export OPEN_AI_KEY={your API key}'
llm = OpenAI(api_token=secret_values, save_charts=False)

df = pd.read_excel('/Users/davidprendez/SoftwareDev/sample_data/Combined_CROP-BRAVE-IPH_DemoClin.xlsx')

smart_df = SmartDataframe(df, config={"llm": llm,"enable_cache": False})
#smart_df.chat('How many data points are there?')

#smart_df.chat('Can you plot the SBP and DBP for Gender? Gender should be 0=Female and 1=Male.')

def ai_viz():
    """
    Produces the text input for the pandasai feature of the app. Users enter their
    prompt directly and then pandasai uploads the corresponding visualization.

    """
    # Set the title of the web app
    st.title("Descriptive Data Visualization for the Brain Artery Network Dataset")
    
    # Get user input using a text input box
    user_input = st.text_input("What would you like to see? For example, type 'Plot the average SBP across different age groups'.")
    
    ai_output = smart_df.chat(user_input)
    
   
    try:
        st.pyplot(ai_output)
    except AttributeError:
        pass
        
    st.write(str(ai_output))

def second_page():
    """
    Sample function for adding extra pages.
    """
    st.title("Second Page")
    st.write("Add content here")

def main():
    """
    Creates a sidebar for navigating through pages and organizes the pages.
    """
    st.sidebar.title("Pages")
    selected_page = st.sidebar.radio("Select a category:", ("Home", "Second Page"))

    if selected_page == "Home":
        ai_viz()
    elif selected_page == "Second Page":
        second_page()

# Run the Streamlit app
if __name__ == "__main__":
    main()
    

