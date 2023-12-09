import unittest
from bava.visualization3d.subject_graph import SubjectGraph

# run 'python -m unittest tests.test_subjectgraph' under SoftwareDev directory
class TestSubjectGraph(unittest.TestCase):
    def setUp(self):
        # Set up a SubjectGraph instance for testing
        self.subject = SubjectGraph('sample_data/tracing_ves_TH_0_7001_U.swc')

    def test_graph_creation(self):
        # Test that a graph was created
        self.assertIsNotNone(self.subject.graph)

    def test_feature_calculation(self):
        # Test that features were calculated
        self.assertIsNotNone(self.subject.features)

    def test_morphological_features(self):
        # Test that local features can be summarized
        morphological_features = self.subject.morphological_features
        self.assertIsNotNone(morphological_features)
        
    def test_graph_features(self):
        # Test that graph features can be retrieved
        graph_features = self.subject.graph_features
        self.assertIsNotNone(graph_features)

if __name__ == '__main__':
    unittest.main()