from .swc2graph import swc2graph, create_interactive_plot
from .graph_analysis import add_centrality_measures, calculate_features, morphological_features, graph_features

class SubjectGraph:
    """
    Represents a subject graph constructed from an SWC file.

    Attributes:
        swc_file (str): The path to the SWC file used to construct the graph.
        graph (Graph): The graph representation of the SWC file.
        features (dict): A dictionary containing calculated features of the graph.

    Methods:
        __init__(self, swc_file): Initializes a new instance of the SubjectGraph class.
        add_centrality_measures(self): Adds centrality measures to the graph.
        summarize_local_features(self): Summarizes the local features of the graph.
        create_interactive_plot(self): Creates an interactive plot of the graph.

    Usage:
        subject_graph = SubjectGraph(swc_file)
        subject_graph.add_centrality_measures()
        local_features = subject_graph.summarize_local_features()
        plot = subject_graph.create_interactive_plot()
    """
    def __init__(self, swc_file):
        self.swc_file = swc_file
        self.graph = swc2graph(self.swc_file)
        self.features = calculate_features(self.graph)

    def add_centrality_measures(self):
        """
        Adds centrality measures to the graph.
        """
        add_centrality_measures(self.graph)

    @property
    def morphological_features(self):
        """
        Summarizes the local features of the graph.

        Returns:
            dict: A dictionary containing the summarized local features.
        """
        return morphological_features(self.features)

    @property
    def graph_features(self):
        """
        Returns the graph features of the graph.

        Returns:
            dict: A dictionary containing the graph features.
        """
        return graph_features(self.graph)

    def create_interactive_plot(self):
        """
        Creates an interactive plot of the graph.

        Returns:
            Plot: An interactive plot of the graph.
        """
        return create_interactive_plot(self.graph)