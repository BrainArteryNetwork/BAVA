import os
import pdb
import glob
import streamlit as st
import plotly.graph_objects as go
import networkx as nx
import numpy as np
from swc2graph import create_interactive_plot, swc2graph
from graph_analysis import add_centrality_measures, graph_analysis

# data_path = '/Users/kennyzhang/UW/Courses/CSE 583 Software Development For Data Scientists/project_git/SoftwareDev/sample_data'
data_path = '/Users/kennyzhang/UW/Courses/CSE 583 Software Development For Data Scientists/project/data/BRAVE'

# Use glob to get a list of SWC files in the data_path directory
file_list = glob.glob(os.path.join(data_path, '*.swc'))

dataset_name = data_path.split('/')[-1]

graphs = {}
# Iterate over the files
for i, file_name in enumerate(file_list):
	# Create the case name
	case_id = file_name.split('/')[-1].split('_')[-2]
	case_name = f"{dataset_name}: {case_id}"
	# Get the full file path
	file_path = os.path.join(data_path, file_name)
	
	# Create the graph object and assign it to the case
	G = swc2graph(file_path)
	add_centrality_measures(G)
	graphs[case_name] = G

# Streamlit app
st.title('Graph Visualization')
# st.set_page_config(layout="wide")

# Sidebar for selecting a case
selected_case = st.sidebar.selectbox('Select a case:', list(graphs.keys()))

# Get the selected graph
G = graphs[selected_case]

# Create the Plotly figure
fig = create_interactive_plot(G)

# Show the figure in Streamlit
st.plotly_chart(fig)
