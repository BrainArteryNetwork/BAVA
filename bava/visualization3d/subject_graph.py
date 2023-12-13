from .swc2graph import swc2graph, create_interactive_plot
from .graph_analysis import add_centrality_measures, calculate_features, calc_morphological_features, calc_graphical_features

class SubjectGraph:
    """
    Represents a subject graph constructed from an SWC file.

    Attributes:
        swc_string (str): The SWC string used to construct the graph.
        graph (Graph): The graph representation of the SWC file.
        features (dict): A dictionary containing calculated features of the graph.

    Methods:
        __init__(self, swc_string): Initializes a new instance of the SubjectGraph class.
        add_centrality_measures(self): Adds centrality measures to the graph.
        summarize_local_features(self): Summarizes the local features of the graph.
        create_interactive_plot(self): Creates an interactive plot of the graph.

    Usage:
        subject_graph = SubjectGraph(swc_string)
        subject_graph.add_centrality_measures()
        local_features = subject_graph.summarize_local_features()
        plot = subject_graph.create_interactive_plot()
    """
    def __init__(self, swc_string):
        self.swc_string = swc_string
        self.graph = swc2graph(self.swc_string)
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
        morph_features = calc_morphological_features(self.features)
        # for each dictionary in morph_features, concat the key with the key in lower level dictionary and copy to a new dictionary
        morph_features_new = {}
        for key, value in morph_features.items():
            for k, v in value.items():
                morph_features_new[key + '_' + k] = v
        return morph_features_new

    @property
    def graphical_features(self):
        """
        Returns the graph features of the graph.

        Returns:
            dict: A dictionary containing the graph features.
        """
        return calc_graphical_features(self.graph)

    def create_interactive_plot(self):
        """
        Creates an interactive plot of the graph.

        Returns:
            Plot: An interactive plot of the graph.
        """
        return create_interactive_plot(self.graph)