import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate centrality measures and add as node attributes
def add_centrality_measures(G):
    nx.set_node_attributes(G, nx.degree_centrality(G), 'degree')
    nx.set_node_attributes(G, nx.closeness_centrality(G), 'closeness')
    nx.set_node_attributes(G, nx.betweenness_centrality(G), 'betweenness')
    # nx.set_node_attributes(G, nx.eigenvector_centrality(G, max_iter=5000), 'eigenvector')
    nx.set_node_attributes(G, nx.pagerank(G), 'pagerank')

def graph_analysis(G):
    
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

    # Output eigenvalues information or any other spectral analysis results
    # print(f'Eigenvalues of the Adjacency Matrix: {eigenvalues_A}')
    # print(f'Eigenvalues of the Laplacian Matrix: {eigenvalues_L}')

def calculate_total_length(G):
    # Extract node positions
    positions = nx.get_node_attributes(G, 'pos')

    # Using list comprehension and numpy for vectorized operations
    distances = [np.linalg.norm(np.array(positions[edge[0]]) - np.array(positions[edge[1]])) 
                 for edge in G.edges()]

    total_length = sum(distances)
    return total_length

def count_branch(G):
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

