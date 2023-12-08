import os
import pdb
import copy
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from .graph_analysis import graph_analysis, add_centrality_measures, calculate_total_length, count_branch, calculate_features, matchvestype, getvesname, summarize_local_features

def create_interactive_plot(G):
    """
    Creates an interactive 3D network graph plot.

    Parameters:
        G (networkx.Graph): The graph object representing the network.

    Returns:
        plotly.graph_objects.Figure: The interactive 3D network graph plot.
    """
    # Extract node positions
    pos = nx.get_node_attributes(G, 'pos')

    # Create color map for vessel types
    vessel_types = set()
    for _, _, edge_data in G.edges(data=True):
        vessel_types.add(edge_data['ves_type'])
    colors = plt.cm.rainbow(np.linspace(0, 1, len(vessel_types)))
    color_map = {getvesname(ves_type): f'rgb({int(255*color[0])}, {int(255*color[1])}, {int(255*color[2])})' 
                 for ves_type, color in zip(vessel_types, colors)}

    # Edge data - creating a trace for each edge
    edge_traces = []
    legend_traces = []
    legend_added = set()
    edge_width = 5
    for edge in G.edges(data=True):
        x0, y0, z0 = pos[edge[0]]
        x1, y1, z1 = pos[edge[1]]
        ves_type = getvesname(edge[2]['ves_type'])
        color = color_map[ves_type]
        edge_trace = go.Scatter3d(x=[x0, x1], y=[y0, y1], z=[z0, z1], mode='lines',
                                  line=dict(color=color, width=edge_width), hoverinfo='text', 
                                  hovertext=ves_type, showlegend=False)
        edge_traces.append(edge_trace)
        if ves_type not in legend_added:
            legend_trace = go.Scatter3d(x=[None], y=[None], z=[None], mode='lines',
                                        line=dict(color=color, width=4), name=ves_type)
            legend_traces.append(legend_trace)
            legend_added.add(ves_type)

    # Node data
    node_opacity = 0.5
    node_x, node_y, node_z, node_color, node_hover_text = [], [], [], [], []
    centrality_eigen = 'eigenvector'
    centrality_betweenness = 'betweenness'
    centrality_closeness = 'closeness'
    for node, data in G.nodes(data=True):
        node_x.append(pos[node][0])
        node_y.append(pos[node][1])
        node_z.append(pos[node][2])
        node_color.append('red' if len(data['ves_type']) > 1 else 'blue')
        hover_text = ', '.join([getvesname(vt) for vt in data['ves_type']])
        
        centrality_betweenness_value = data.get(centrality_betweenness, 0)  # Default to 0 if not found
        hover_text += f"<br>{centrality_betweenness.capitalize()}: {centrality_betweenness_value*10000:.2f}"
        
        centrality_closeness_value = data.get(centrality_closeness, 0)  # Default to 0 if not found
        hover_text += f"<br>{centrality_closeness.capitalize()}: {centrality_closeness_value*10000:.2f}"
        
        centrality_eigen_value = data.get(centrality_eigen, 0)  # Default to 0 if not found
        hover_text += f"<br>{'Eigen Centrality'}: {centrality_eigen_value*10000:.2f}"
        
        node_hover_text.append(hover_text)

    node_trace = go.Scatter3d(x=node_x, y=node_y, z=node_z, mode='markers',
                              marker=dict(size=3.5, color=node_color), hoverinfo='text', 
                              hovertext=node_hover_text, opacity=node_opacity, showlegend=False)

    # Define layout
    layout = go.Layout(
        title='Advanced 3D Network Graph',
        scene=dict(
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, showbackground=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, showbackground=False),
            zaxis=dict(showgrid=False, zeroline=False, showticklabels=False, showbackground=False),
        ),
        legend=dict(title='Vessel Types')
    )

    # Create and return the figure
    fig = go.Figure(data=edge_traces + legend_traces + [node_trace], layout=layout)
    return fig

def visualize_3d_graph(G):
    """
    Visualizes a 3D graph.

    Parameters:
        G (networkx.Graph): The graph to visualize.

    Returns:
        None
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    pos = nx.get_node_attributes(G, 'pos')  # Position should be a tuple (x, y, z)

    # Extract the x, y, z coordinates of each node
    xs, ys, zs = zip(*[pos[v] for v in G.nodes()])
    
    # Draw the nodes
    ax.scatter(xs, ys, zs, color='gray', s=20)  # Nodes in gray, adjust size as needed

    # Create a color map for vessel types
    vessel_types = []
    for _, _, edge_data in G.edges(data=True):
        vessel_types.append(getvesname(edge_data.get('ves_type', [])))
    # remove the duplicate vessel types
    vessel_types = list(set(vessel_types))

    colors = plt.cm.rainbow(np.linspace(0, 1, len(vessel_types)))
    color_map = {ves_type: color for ves_type, color in zip(vessel_types, colors)}

    # Draw the edges in different colors based on vessel type
    for edge in G.edges(data=True):
        x, y, z = zip(*[pos[v] for v in edge[:2]])
        ves_type = getvesname(edge[2].get('ves_type', [None]))  # Get the first vessel type of the edge
        color = color_map.get(ves_type, 'black')  # Default to black if no type
        ax.plot(x, y, z, color=color)

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    plt.title("3D Graph Visualization")

    # Create a legend for vessel types
    legend_elements = [plt.Line2D([0], [0], color=color_map[vt], lw=2, label=vt) for vt in vessel_types]
    ax.legend(handles=legend_elements, title="Vessel Types")

    plt.show()


def generateG(all_selected_points, all_selected_points_rad, all_selected_points_id, all_selected_points_type):
    """
    Generate a graph representation of a 3D structure based on selected points.

    Parameters:
    - all_selected_points (list of lists): A list of lists containing the coordinates of selected points.
    - all_selected_points_rad (list of lists): A list of lists containing the radii of the selected points.
    - all_selected_points_id (list of lists): A list of lists containing the IDs of the selected points.
    - all_selected_points_type (list of lists): A list of lists containing the types of the selected points.

    Returns:
    - G (networkx.Graph): A graph representation of the 3D structure, where nodes represent points and edges represent connections between points.
    """

    G = nx.Graph()

    # Mapping from position to node ID
    position_to_id_map = {}
    node_attributes = {}

    for segment_points, segment_ids, segment_rads, segment_types in zip(all_selected_points, all_selected_points_id, all_selected_points_rad, all_selected_points_type):
        # Determine vessel type for the segment
        ves_type = matchvestype(int(segment_types[0]), int(segment_types[-1]))

        for point, id, rad in zip(segment_points, segment_ids, segment_rads):
            pos_key = tuple(point)
            if pos_key not in position_to_id_map:
                position_to_id_map[pos_key] = id
                node_attributes[id] = {'pos': point, 'radius': rad, 'ves_type': [ves_type]}
            else:
                # For bifurcation points, append vessel type to list
                existing_id = position_to_id_map[pos_key]
                if ves_type not in node_attributes[existing_id]['ves_type']:
                    node_attributes[existing_id]['ves_type'].append(ves_type)

    # Add nodes to the graph
    for id, attrs in node_attributes.items():
        G.add_node(id, **attrs)

    # Add edges to the graph, assigning vessel type
    for segment_points, segment_ids, segment_types in zip(all_selected_points, all_selected_points_id, all_selected_points_type):
        # Determine vessel type for the segment
        ves_type = matchvestype(int(segment_types[0]), int(segment_types[-1]))

        for i in range(len(segment_ids) - 1):
            start_pos = tuple(segment_points[i])
            end_pos = tuple(segment_points[i + 1])
            start_id = position_to_id_map[start_pos]
            end_id = position_to_id_map[end_pos]

            # Determine edge vessel type
            # If a node is a bifurcation point, use the vessel type from the other node
            if len(node_attributes[start_id]['ves_type']) > 1:  # start_id is a bifurcation point
                edge_ves_type = node_attributes[end_id]['ves_type'][0]
            elif len(node_attributes[end_id]['ves_type']) > 1:  # end_id is a bifurcation point
                edge_ves_type = node_attributes[start_id]['ves_type'][0]
            else:
                edge_ves_type = ves_type

            G.add_edge(start_id, end_id, ves_type=edge_ves_type)

    return G

def swc2graph(swcfilename, distance_threshold=10):
    """
    Convert an SWC file to a graph representation.

    Parameters:
    - swcfilename (str): The path to the SWC file.
    - distance_threshold (float): The distance threshold for selecting points along the snakes.

    Returns:
    - graph (Graph): The graph representation of the SWC file.
    """

    swclist = []
    if not os.path.exists(swcfilename):
        print("not exist", swcfilename)
        return swclist

    swc_data = np.loadtxt(swcfilename)
    swc_data_transform = copy.deepcopy(swc_data)

    # Find the indices where the last column is -1
    root_indices = np.where(swc_data_transform[:, -1] == -1)[0]
    # Create a list to hold the individual "snakes"
    snakes = []
    all_selected_points = []
    all_selected_points_rad = []
    all_selected_points_id = []
    all_selected_points_type = []
    all_selected_points_pid = []

    # STEP 1: Select points along the snakes
    for i in range(len(root_indices) - 1):
        # Get the slice of swc_data between two root indices
        swc_snake = swc_data_transform[root_indices[i] : root_indices[i + 1]]
        # select the third to fifth columns and form a numpy array
        swc_snake_pos = swc_snake[:, 2:5]
        swc_snake_rad = swc_snake[:, 5]
        swc_snake_id = swc_snake[:, 0]
        swc_snake_type = swc_snake[:, 1]
        swc_snake_pid = swc_snake[:, -1]
        # calculate the distance between two adjacent points
        distances = np.sqrt(np.sum(np.diff(swc_snake_pos, axis=0) ** 2, axis=1))

        # Initialize a list to store the selected points
        selected_points = [swc_snake_pos[0]]  # always include the first point
        selected_points_rad = [swc_snake_rad[0]]
        selected_points_id = [swc_snake_id[0]]
        selected_points_type = [swc_snake_type[0]]
        selected_points_pid = [swc_snake_pid[0]]
        # Initialize a variable to keep track of the cumulative distance
        cumulative_distance = 0

        # Loop over the distances
        for ii in range(1, len(distances)):
            # Add the current distance to the cumulative distance
            cumulative_distance += distances[ii - 1]
            # If the cumulative distance is greater than or equal to the threshold
            if cumulative_distance >= distance_threshold:
                # Add the current point to the list of selected points
                selected_points.append(swc_snake_pos[ii])
                selected_points_rad.append(swc_snake_rad[ii])
                selected_points_id.append(swc_snake_id[ii])
                selected_points_type.append(swc_snake_type[ii])
                selected_points_pid.append(swc_snake_pid[ii])
                # Reset the cumulative distance
                cumulative_distance = 0

        # Always include the last point
        if not np.array_equal(selected_points[-1], swc_snake_pos[-1]):
            selected_points.append(swc_snake_pos[-1])
            selected_points_rad.append(swc_snake_rad[-1])
            selected_points_id.append(swc_snake_id[-1])
            selected_points_type.append(swc_snake_type[-1])
            selected_points_pid.append(swc_snake_pid[-1])

        selected_points = np.array(selected_points)
        all_selected_points.append(selected_points)
        all_selected_points_rad.append(np.array(selected_points_rad))
        all_selected_points_id.append(np.array(selected_points_id))
        all_selected_points_type.append(np.array(selected_points_type))
        all_selected_points_pid.append(np.array(selected_points_pid))

        # loop over the rows of snake_pos and create a PointROI for each row
        # snake = Snake([PointROI(pos) for pos in selected_points])
        # snake.label = ves_type_swc

    # graph = generateG(all_selected_points[:100], all_selected_points_rad[:100], all_selected_points_id[:100], all_selected_points_type[:100])
    graph = generateG(all_selected_points, all_selected_points_rad, all_selected_points_id, all_selected_points_type)

    return graph

# # for temporary test of visualization and feature output
# test_case = "/Users/kennyzhang/UW/Courses/CSE 583 Software Development For Data Scientists/project_git/SoftwareDev/sample_data/tracing_ves_TH_0_7001_U.swc"
# test_case2 = "/Users/kennyzhang/UW/Courses/CSE 583 Software Development For Data Scientists/project_git/SoftwareDev/sample_data/tracing_ves_TH_0_7002_U.swc"

# graph = swc2graph(test_case)
# graph2 = swc2graph(test_case2)

# length = calculate_total_length(graph)
# length2 = calculate_total_length(graph2)
# print(f'Total length: {length}, {length2}')
# branches = count_branch(graph)
# branches2 = count_branch(graph2)
# print(f'Total branches: {branches}, {branches2}')

# pdb.set_trace()

# feature_dict = calculate_features(graph)
# summarize_dict = summarize_local_features(feature_dict)

# # graph_analysis(graph)
# # add_centrality_measures(graph)

# fig = create_interactive_plot(graph)
# # Show the plot
# fig.show()

# # visualize_3d_graph(graph)
