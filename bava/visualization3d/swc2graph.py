import os
import pdb
import copy
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go

BOITYPENUM = 23
VESTYPENUM = 25

# Old iCafe definition
def getvesname(id):
    VesselName = [None for i in range(VESTYPENUM)]
    VesselName[1] = "ICA_L"
    VesselName[2] = "ICA_R"
    VesselName[3] = "M1_L"
    VesselName[4] = "M1_R"
    VesselName[5] = "M2_L"
    VesselName[6] = "M2_R"
    VesselName[7] = "A1_L"
    VesselName[8] = "A1_R"
    VesselName[9] = "A2_L"
    VesselName[10] = "A2_R"
    VesselName[11] = "AComm"
    VesselName[12] = "M3_L"
    VesselName[13] = "M3_R"
    VesselName[14] = "VA_L"
    VesselName[15] = "VA_R"
    VesselName[16] = "BA"
    VesselName[17] = "P1_L"
    VesselName[18] = "P1_R"
    VesselName[19] = "P2_L"
    VesselName[20] = "P2_R"
    VesselName[21] = "PComm_L"
    VesselName[22] = "PComm_R"
    VesselName[23] = "OA_L"
    VesselName[24] = "OA_R"
    return VesselName[id]

def create_interactive_plot(G):
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
    for node, data in G.nodes(data=True):
        node_x.append(pos[node][0])
        node_y.append(pos[node][1])
        node_z.append(pos[node][2])
        node_color.append('red' if len(data['ves_type']) > 1 else 'blue')
        node_hover_text.append(', '.join([getvesname(vt) for vt in data['ves_type']]))

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

def matchvestype(starttype, endtype):
    EndCondition = np.zeros((100, 100), dtype=np.int8)
    EndCondition[1][3] = 1
    EndCondition[2][4] = 2
    EndCondition[3][1] = 1
    EndCondition[3][5] = 7
    EndCondition[3][7] = 3
    EndCondition[4][2] = 2
    EndCondition[4][8] = 4
    EndCondition[4][6] = 8
    EndCondition[5][6] = 11
    EndCondition[5][3] = 7
    EndCondition[5][23] = 9
    EndCondition[5][99] = 9
    EndCondition[6][4] = 8
    EndCondition[6][5] = 11
    EndCondition[6][24] = 10
    EndCondition[6][99] = 10
    EndCondition[7][3] = 3
    EndCondition[7][13] = 5
    EndCondition[7][29] = 5
    EndCondition[7][99] = 5
    EndCondition[8][4] = 4
    EndCondition[8][14] = 6
    EndCondition[8][30] = 6
    EndCondition[8][99] = 6
    EndCondition[9][11] = 23
    EndCondition[10][12] = 24
    EndCondition[11][9] = 23
    EndCondition[12][10] = 24
    EndCondition[13][7] = 5
    EndCondition[13][99] = 12
    EndCondition[13][25] = 12
    EndCondition[13][29] = 5
    EndCondition[14][8] = 6
    EndCondition[14][99] = 13
    EndCondition[14][26] = 13
    EndCondition[14][30] = 6
    EndCondition[15][17] = 14
    EndCondition[16][17] = 15
    EndCondition[17][15] = 14
    EndCondition[17][16] = 15
    EndCondition[17][18] = 16
    EndCondition[18][17] = 16
    EndCondition[18][20] = 18
    EndCondition[18][19] = 17
    EndCondition[19][18] = 17
    EndCondition[19][21] = 21
    EndCondition[19][99] = 19
    EndCondition[19][27] = 19
    EndCondition[20][22] = 22
    EndCondition[20][18] = 18
    EndCondition[20][99] = 20
    EndCondition[20][28] = 20
    EndCondition[21][19] = 21
    EndCondition[22][20] = 22
    EndCondition[23][99] = 9
    EndCondition[23][5] = 9
    EndCondition[23][23] = 9
    EndCondition[24][99] = 10
    EndCondition[24][6] = 10
    EndCondition[24][24] = 10
    EndCondition[25][99] = 12
    EndCondition[25][13] = 12
    EndCondition[25][25] = 12
    EndCondition[26][99] = 13
    EndCondition[26][14] = 13
    EndCondition[26][26] = 13
    EndCondition[27][99] = 19
    EndCondition[27][19] = 19
    EndCondition[27][27] = 19
    EndCondition[28][99] = 20
    EndCondition[28][20] = 20
    EndCondition[28][28] = 20
    EndCondition[29][7] = 5
    EndCondition[29][13] = 5
    EndCondition[29][29] = 5
    EndCondition[29][99] = 5
    EndCondition[30][8] = 6
    EndCondition[30][14] = 6
    EndCondition[30][30] = 6
    EndCondition[30][99] = 6
    return EndCondition[starttype][endtype]
    # return getvesname(EndCondition[starttype][endtype])

def generateG(all_selected_points, all_selected_points_rad, all_selected_points_id, all_selected_points_type):
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

    graph = generateG(all_selected_points[:100], all_selected_points_rad[:100], all_selected_points_id[:100], all_selected_points_type[:100])
    # generateG(all_selected_points, all_selected_points_rad, all_selected_points_id, all_selected_points_type)

    return graph


test_case = "/Users/kennyzhang/UW/Courses/CSE 583 Software Development For Data Scientists/project_git/SoftwareDev/sample_data/tracing_ves_TH_0_7001_U.swc"

graph = swc2graph(test_case)

fig = create_interactive_plot(graph)
# Show the plot
fig.show()

# visualize_3d_graph(graph)
