import networkx as nx


ba_graph = nx.barabasi_albert_graph(200, 5, 3)  # Example parameters (n=200 nodes, m0=5 Initial number of nodes, m = 3  # Number of edges to attach from a new node to existing nodes)

def calculate_network_properties(G):
    """Calculate various properties of the network.

    Parameters:
    G (networkx.Graph): The graph for which to calculate properties.

    Returns:
    properties (dict): Dictionary containing network properties.
    """
    properties = {}

    # Diameter: Longest shortest path in the network
    if nx.is_connected(G):
        properties['diameter'] = nx.diameter(G)
    else:
        properties['diameter'] = "undefined (disconnected graph)"

    # Clustering Coefficient: Measure of degree to which nodes tend to cluster together
    properties['average_clustering_coefficient'] = nx.average_clustering(G)

    # Degree Distribution: Probability distribution of the degrees over the network
    degrees = [G.degree(n) for n in G.nodes()]
    properties['degree_distribution'] = degrees

    return properties

# Calculate network properties for the BA model graph
ba_properties = calculate_network_properties(ba_graph)

# Output the calculated properties
print(ba_properties)
