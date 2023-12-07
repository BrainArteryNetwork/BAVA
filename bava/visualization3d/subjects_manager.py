from .subject_graph import SubjectGraph

class SubjectsManager:
    def __init__(self):
        self.subjects = {}

    def add_subject(self, identifier, swc_file):
        self.subjects[identifier] = SubjectGraph(swc_file)

    def get_subject(self, identifier):
        return self.subjects.get(identifier, None)
    
    # write a method to get all subjects' identifiers
    def get_all_subjects(self):
        return list(self.subjects.keys())
        
            
# if __name__ == "__main__":
#     # Create an instance of SubjectsManager
#     manager = SubjectsManager()

#     # Test the add_subject method
#     manager.add_subject('subject1', '/Users/kennyzhang/UW/Courses/CSE 583 Software Development For Data Scientists/project_git/SoftwareDev/sample_data/tracing_ves_TH_0_7001_U.swc')
#     manager.add_subject('subject2', '/Users/kennyzhang/UW/Courses/CSE 583 Software Development For Data Scientists/project_git/SoftwareDev/sample_data/tracing_ves_TH_0_7002_U.swc')

#     # Test the get_subject method
#     subject1 = manager.get_subject('subject1')
#     print(subject1)

#     subject2 = manager.get_subject('subject2')
#     print(subject2)

#     # Test getting a subject that doesn't exist
#     non_existent_subject = manager.get_subject('non_existent_subject')
#     print(non_existent_subject)  # Should print None