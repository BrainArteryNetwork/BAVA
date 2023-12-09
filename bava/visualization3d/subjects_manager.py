from .subject_graph import SubjectGraph

class SubjectsManager:
    """
    A class that manages subjects and their associated data.

    Attributes:
        subjects (dict): A dictionary that stores the subjects, where the keys are the subject identifiers
                         and the values are the corresponding SubjectGraph objects.

    Methods:
        __init__(): Initializes an empty SubjectsManager object.
        add_subject(identifier, swc_file): Adds a new subject to the manager with the given identifier and SWC file.
        get_subject(identifier): Retrieves the subject with the given identifier from the manager.
        get_all_subjects(): Returns a list of all subject identifiers in the manager.
    """

    def __init__(self):
        """
        Initializes an empty SubjectsManager object.
        """
        self.subjects = {}

    def add_subject(self, identifier, swc_file):
        """
        Adds a new subject to the manager with the given identifier and SWC file.

        Args:
            identifier (str): The identifier of the subject.
            swc_file (str): The file path of the SWC file associated with the subject.
        """
        self.subjects[identifier] = SubjectGraph(swc_file)

    def get_subject(self, identifier):
        """
        Retrieves the subject with the given identifier from the manager.

        Args:
            identifier (str): The identifier of the subject.

        Returns:
            SubjectGraph or None: The SubjectGraph object associated with the identifier,
                                 or None if the identifier is not found.
        """
        return self.subjects.get(identifier, None)

    def get_all_subjects(self):
        """
        Returns a list of all subject identifiers in the manager.

        Returns:
            list: A list of all subject identifiers.
        """
        return list(self.subjects.keys())
