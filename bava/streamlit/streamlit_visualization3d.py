import os
import pdb
import glob
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import networkx as nx
import numpy as np
from bava.visualization3d.subjects_manager import SubjectsManager
import plotly.graph_objects as go

# run with 'streamlit run ./bava/streamlit/streamlit_visualization3d.py' under SoftwareDev directory

def page_viz3d():
	"""
	Main function for graph visualization.

	This function reads SWC files from a specified directory, creates graph objects from the SWC files,
	calculates centrality measures for each graph, and visualizes the selected graph using Plotly.

	"""

	# (temporary) will be removed when connecting to the database
	df = pd.read_excel('./sample_data/Combined_CROP-BRAVE-IPH_DemoClin.xlsx')
 
	# Create a filter bar for age
	age_range = st.sidebar.slider('Age Range', min(df['Age']), max(df['Age']), (min(df['Age']), max(df['Age'])))
	min_age, max_age = age_range

	# Filter the DataFrame based on the selected age range
	filtered_df = df[(df['Age'] >= min_age) & (df['Age'] <= max_age)]

	# Create a checkbox for diabetes
	diabetes_option = st.sidebar.checkbox('Diabetes')

	# Filter the DataFrame based on the selected diabetes option
	if diabetes_option:
		filtered_df = filtered_df[filtered_df['Diabetes'] > 0]
	else:
		filtered_df = filtered_df[filtered_df['Diabetes'] == 0]

	# Create checkboxes for race
	race_options = ['Native American', 'Pacific Islander', 'Asian', 'Caucasian', 'African American', 'Multiple Races', 'Other']
	race_values = [1, 2, 3, 4, 5, 6, 7]
	selected_races = st.sidebar.multiselect('Race', race_options, default=race_options)

	# Map the selected races to their corresponding values
	selected_race_values = [race_values[race_options.index(race)] for race in selected_races]

	# Filter the DataFrame based on the selected race options
	filtered_df = filtered_df[filtered_df['Race'].isin(selected_race_values)]

	# Display the filtered DataFrame
	st.dataframe(filtered_df)

	data_path = './sample_data'
	# data_path = '/Users/kennyzhang/UW/Courses/CSE 583 Software Development For Data Scientists/project/data/BRAVE'

	# Use glob to get a list of SWC files in the data_path directory
	file_list = glob.glob(os.path.join(data_path, '*.swc'))

	dataset_name = data_path.split('/')[-1]

	manager = SubjectsManager()
	# Iterate over the files
	for i, file_name in enumerate(file_list):
		# Create the case name
		case_id = file_name.split('/')[-1].split('_')[-2]
		case_name = f"{dataset_name}: {case_id}"
		# Get the full file path
		file_path = file_name
		# file_path = os.path.join(data_path, file_name)

		# Create the graph object and assign it to the case
		manager.add_subject(case_name, file_path)

	# Streamlit app
	st.title('Graph Visualization')
	# st.set_page_config(layout="wide")

	# Sidebar for selecting a case
	selected_case = st.sidebar.selectbox('Select a case:', manager.get_all_subjects())

	# Get the selected graph
	G = manager.get_subject(selected_case)

	# Create the Plotly figure
	fig = G.create_interactive_plot()

	# Show the figure in Streamlit
	st.plotly_chart(fig)

if __name__ == "__main__":
	page_viz3d()
