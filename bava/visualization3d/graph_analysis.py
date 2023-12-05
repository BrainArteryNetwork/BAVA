"""
This module provides functions for performing graph analysis on a given graph.

The main function, `graph_analysis`, calculates various graph metrics and performs spectral analysis on the graph.

Example usage:
    import networkx as nx
    import numpy as np
    import matplotlib.pyplot as plt

    G = nx.Graph()
    # Add nodes and edges to the graph

    graph_analysis(G)
"""
import re
import pdb
import math
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate centrality measures and add as node attributes
def add_centrality_measures(G):
    """
    Add centrality measures as node attributes to the given graph.

    Parameters:
    - G (networkx.Graph): The input graph to which centrality measures will be added.

    Returns:
    None
    """
    nx.set_node_attributes(G, nx.degree_centrality(G), 'degree')
    nx.set_node_attributes(G, nx.closeness_centrality(G), 'closeness')
    nx.set_node_attributes(G, nx.betweenness_centrality(G), 'betweenness')
    # nx.set_node_attributes(G, nx.eigenvector_centrality(G, max_iter=5000), 'eigenvector')
    nx.set_node_attributes(G, nx.pagerank(G), 'pagerank')

def graph_analysis(G):
    """
    Perform graph analysis on a given graph.

    Parameters:
    - G (networkx.Graph): The input graph for analysis.

    Returns:
    None
    """

    # Basic Graph Metrics
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    degrees = [degree for node, degree in G.degree()]
    clustering_coeffs = nx.clustering(G)
    avg_clustering_coeff = nx.average_clustering(G)
    path_lengths = dict(nx.shortest_path_length(G))
    betweenness = nx.betweenness_centrality(G)
    closeness = nx.closeness_centrality(G)
    # eigenvector = nx.eigenvector_centrality(G, max_iter=1000)
    components = [comp for comp in nx.connected_components(G)]
    largest_component = max(components, key=len)
    if nx.is_connected(G):
        diameter = nx.diameter(G)
        radius = nx.radius(G)
    assortativity = nx.degree_assortativity_coefficient(G)

    # Graph Spectral Analysis
    # Adjacency Matrix
    A = nx.convert_matrix.to_numpy_array(G)

    # Laplacian Matrix
    L = nx.laplacian_matrix(G).toarray()

    # Eigenvalues and Eigenvectors
    eigenvalues_A, eigenvectors_A = np.linalg.eig(A)
    eigenvalues_L, eigenvectors_L = np.linalg.eig(L)

    # Sort eigenvalues for plotting
    sorted_eigenvalues_L = np.sort(eigenvalues_L)

    # Plotting the Eigenvalue Spectrum of the Laplacian
    plt.plot(sorted_eigenvalues_L, 'o')
    plt.title('Eigenvalue Spectrum of the Laplacian')
    plt.xlabel('Index')
    plt.ylabel('Eigenvalue')
    plt.show()

    # Output the basic graph metrics
    print(f'Number of Nodes: {num_nodes}')
    print(f'Number of Edges: {num_edges}')
    print(f'Average Degree: {np.mean(degrees)}')
    print(f'Average Clustering Coefficient: {avg_clustering_coeff}')
    # print(f'Betweenness Centrality: {betweenness}')
    # print(f'Closeness Centrality: {closeness}')
    # print(f'Eigenvector Centrality: {eigenvector}')
    print(f'Number of Connected Components: {len(components)}')
    print(f'Largest Component Size: {len(largest_component)}')
    print(f'Diameter (if connected): {diameter if nx.is_connected(G) else "N/A"}')
    print(f'Radius (if connected): {radius if nx.is_connected(G) else "N/A"}')
    print(f'Assortativity: {assortativity}')

def calculate_total_length(G):
    """
    Calculate the total length of all edges in the graph.

    Parameters:
    - G (networkx.Graph): The input graph.

    Returns:
    - total_length (float): The total length of all edges in the graph.
    """
    # Extract node positions
    positions = nx.get_node_attributes(G, 'pos')

    # Using list comprehension and numpy for vectorized operations
    distances = [np.linalg.norm(np.array(positions[edge[0]]) - np.array(positions[edge[1]])) 
                 for edge in G.edges()]

    total_length = sum(distances)
    return total_length

def count_branch(G):
    """
    Counts the number of branches in a graph.

    Parameters:
    - G (networkx.Graph): The input graph.

    Returns:
    - int: The total number of branches in the graph.
    """
    def is_branching_point(node):
        return G.degree[node] != 2

    visited_edges = set()

    def traverse_branch(node, prev=None):
        if is_branching_point(node) and node != prev:
            return 1  # Found the end of a branch
        branches = 0
        for neighbor in G.neighbors(node):
            if neighbor != prev:
                edge = tuple(sorted([node, neighbor]))
                if edge not in visited_edges:
                    visited_edges.add(edge)
                    branches += traverse_branch(neighbor, node)
        return branches

    total_branches = 0
    for node in G.nodes():
        if is_branching_point(node):
            total_branches += traverse_branch(node)
    
    return total_branches // 2  # Divide by 2 as each branch is counted twice

def calculate_features(G):
    """
    Calculate the length, branch number, and tortuosity for each type of artery based on the ves_type attribute of the nodes.

    Parameters:
    - G (networkx.Graph): The input graph.

    Returns:
    - artery_features (dict): A dictionary where the keys are ves_type and the values are dictionaries containing the length, branch number, and tortuosity for each type of artery.
    """
    # Initialize the dictionary to store artery features
    artery_features = {}

    # Iterate over the edges in the graph
    for edge in G.edges():
        node1, node2 = edge
        edge_type = getvesname(G.edges[edge]['ves_type'])
        
        if edge_type not in artery_features:
            artery_features[edge_type] = {'length': 0, 'branch_number': 0}

        # Calculate the length of the edge
        length = np.linalg.norm(np.array(G.nodes[node1]['pos']) - np.array(G.nodes[node2]['pos']))

        # Add the length, branch number, and tortuosity to the corresponding artery
        artery_features[edge_type]['length'] += length

        # Check if the edge is a branch
        if G.degree[node1] != 2 or G.degree[node2] != 2:
            artery_features[edge_type]['branch_number'] += 1

    # Divide the branch number by 2 as each branch is counted twice
    for artery in artery_features:
        artery_features[artery]['branch_number'] = math.ceil(artery_features[artery]['branch_number'] / 2)

    return artery_features

def summarize_local_features(feature_dict):

    # Initialize the subregions
    subregions = ["ACA", "MCA", "PCA"]
    sides = ["L", "R"]
    proximities = ["proximal", "distal"]

    # Initialize the results for the subregions
    subregion_results = {}

    # Iterate through the subregions, sides and proximities
    for subregion in subregions:
        subregion_character = subregion[0]
        for side in sides:
            for proximity in proximities:
                # Initialize the total length, total branches and total tortuosity
                total_length = 0
                total_branches = 0
                count = 0

                # Iterate through the snakes
                for ves_type, ves_features in feature_dict.items():
                    # Check if the snake type matches the subregion, side and proximity
                    if (
                        re.compile("{}.*_.*".format(subregion_character)).match(
                            ves_type
                        )
                        and side in ves_type
                        and (
                            (
                                proximity == "proximal"
                                and "2" not in ves_type
                                and "3" not in ves_type
                            )
                            or (
                                proximity == "distal"
                                and ("2" in ves_type or "3" in ves_type)
                            )
                        )
                    ):
                        # Add the snake features to the total features
                        total_length += ves_features['length']
                        total_branches += ves_features['branch_number']
                        count += 1

                # Add the subregion results to the results
                subregion_results[f"{proximity}_{subregion}_{side}"] = [
                    total_length,
                    total_branches,
                ]

    def merge_subregion_results(subregion_results):
        merged_results = {}

        for subregion_key, subregion_value in subregion_results.items():
            # Split the key into its components
            components = subregion_key.split("_")

            # Create new keys by fixing two components and merging the third
            for i in range(3):
                new_key = "_".join(components[:i] + components[i + 1 :])
                if new_key not in merged_results:
                    # Sum the first two values and calculate the average of the third value
                    merged_results[new_key] = subregion_value
                else:
                    # Add the values if the key already exists
                    merged_results[new_key] = [
                        x + y if idx < 2 else (x + y) / 2
                        for idx, (x, y) in enumerate(zip(merged_results[new_key], subregion_value))
                    ]
        return merged_results

    def further_merge(merged_results):
        further_merged_results = {}
        keys_to_merge = ["R", "L", "MCA", "ACA", "PCA", "proximal", "distal"]

        for key in keys_to_merge:
            for merged_key, merged_value in merged_results.items():
                if key in merged_key:
                    if key not in further_merged_results:
                        further_merged_results[key] = merged_value
                    else:
                        # Add the values if the key already exists
                        further_merged_results[key] = [
                                x + y if idx < 2 else (x + y) / 2
                            for idx, (x, y) in enumerate(zip(further_merged_results[key], merged_value))
                        ]
        return further_merged_results

    merged_results = merge_subregion_results(subregion_results)
    further_merged_results = further_merge(merged_results)
    # calculate the total length, total branch number and average tortuosity based on further_merged_results
    total_length = (
        further_merged_results["proximal"][0] + further_merged_results["distal"][0]
    )
    total_branches = (
        further_merged_results["proximal"][1] + further_merged_results["distal"][1]
    )

    total_results = {"total": [total_length, total_branches]}
    
    def dictvalue2dict(dictionary):
        # Convert the previous dictionary value from list [value1, value2] to dictionary with format {length: value1, branch_number: value2}
        converted_dict = {}
        for key, value in dictionary.items():
            converted_dict[key] = {
                'length': value[0],
                'branch_number': value[1]
            }
        return converted_dict

    # concat results, merged_results, further_merged_results
    feature_dict = {
        **feature_dict,
        **dictvalue2dict(subregion_results),
        **dictvalue2dict(merged_results),
        **dictvalue2dict(further_merged_results),
        **dictvalue2dict(total_results),
    }
    return feature_dict

BOITYPENUM = 23
VESTYPENUM = 25

# Old iCafe definition
def getvesname(id):
    """
    Returns the name of a vessel based on its ID.

    Parameters:
    id (int): The ID of the vessel.

    Returns:
    str: The name of the vessel corresponding to the given ID.
    """
    VESTYPENUM = 25
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

def matchvestype(starttype, endtype):
    """
    Returns the value from the EndCondition matrix based on the given starttype and endtype.

    Parameters:
    starttype (int): The start type.
    endtype (int): The end type.

    Returns:
    int: The value from the EndCondition matrix.

    """
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