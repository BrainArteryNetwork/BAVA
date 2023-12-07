import os
import pdb
import glob
import streamlit as st
import plotly.graph_objects as go
import networkx as nx
import numpy as np
from bava.visualization3d.subjects_manager import SubjectsManager
import plotly.graph_objects as go

# run with 'streamlit run ./bava/streamlit/streamlit_visualization3d.py' under SoftwareDev directory

def main():
	"""
	Main function for graph visualization.

	This function reads SWC files from a specified directory, creates graph objects from the SWC files,
	calculates centrality measures for each graph, and visualizes the selected graph using Plotly.

	"""

	data_path = '/Users/kennyzhang/UW/Courses/CSE 583 Software Development For Data Scientists/project_git/SoftwareDev/sample_data'
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
		file_path = os.path.join(data_path, file_name)

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
	main()
