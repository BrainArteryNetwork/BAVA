from .swc2graph import swc2graph, create_interactive_plot
from .graph_analysis import add_centrality_measures, calculate_features, summarize_local_features

class SubjectGraph:
    def __init__(self, swc_file):
        self.swc_file = swc_file
        self.graph = swc2graph(self.swc_file)
        self.features = calculate_features(self.graph)

    def add_centrality_measures(self):
        add_centrality_measures(self.graph)

    def summarize_local_features(self):
        summarized_features = summarize_local_features(self.features)
        return summarized_features

    def create_interactive_plot(self):
        return create_interactive_plot(self.graph)
        
# if __name__ == "__main__":
#     # Create an instance of SubjectGraph
#     subject = SubjectGraph('/Users/kennyzhang/UW/Courses/CSE 583 Software Development For Data Scientists/project_git/SoftwareDev/sample_data/tracing_ves_TH_0_7001_U.swc')

#     # Test the add_centrality_measures method
#     subject.add_centrality_measures()

#     # Test the summarize_local_features method
#     summarized_features = subject.summarize_local_features()
#     print(summarized_features)

#     # Test the create_interactive_plot method
#     fig = subject.create_interactive_plot()
#     fig.show()