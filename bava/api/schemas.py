""""""
from enum import Enum
from typing import Optional, List, Tuple
from pydantic import BaseModel

from sqlmodel import Field, SQLModel, Column
from sqlalchemy.types import PickleType

class Gender(Enum):
    """
    Represents the gender of a person.
    """
    female = 0
    male = 1

class Race(Enum):
    """
    Enum representing different races.
    
    Attributes:
        american_indian (int): Represents the American Indian race.
        native_hawaiian (int): Represents the Native Hawaiian race.
        asian (int): Represents the Asian race.
        caucasian (int): Represents the Caucasian race.
        african_american (int): Represents the African American race.
        multiple_race (int): Represents multiple races.
        not_provided (int): Represents when race information is not provided.
    """
    american_indian = 1
    native_hawaiian = 2
    asian = 3
    caucasian = 4
    african_american = 5
    multiple_race = 6
    not_provided = 7


class Info(BaseModel):
    """
    """
    min: int | float = 0
    max: int | float = 0
    avg: float = 0


class MorphologicalFeatures(BaseModel):
    """
    Represents the features of an artery.

    Attributes:
        length (float): The length of the artery.
        branch_number (int): The number of branches in the artery.
        L_length (float): The length of the left artery.
        L_branch_number (int): The number of branches in the left artery.
        proximal_L_length (float): The length of the proximal left artery.
        proximal_L_branch_number (int): The number of branches in the proximal left artery.
        distal_L_length (float): The length of the distal left artery.
        distal_L_branch_number (int): The number of branches in the distal left artery.
        R_length (float): The length of the right artery.
        R_branch_number (int): The number of branches in the right artery.
        proximal_R_length (float): The length of the proximal right artery.
        proximal_R_branch_number (int): The number of branches in the proximal right artery.
        distal_R_length (float): The length of the distal right artery.
        distal_R_branch_number (int): The number of branches in the distal right artery.
        proximal_length (float): The length of the proximal artery.
        proximal_branch_number (int): The number of branches in the proximal artery.
        distal_length (float): The length of the distal artery.
        distal_branch_number (int): The number of branches in the distal artery.
        PComm_L_length (float): The length of the posterior communicating artery on the left side.
        PComm_L_branch_number (int): The number of branches in the posterior communicating artery on the left side.
        PComm_R_length (float): The length of the posterior communicating artery on the right side.
        PComm_R_branch_number (int): The number of branches in the posterior communicating artery on the right side.
        AComm_length (float): The length of the anterior communicating artery.
        AComm_branch_number (int): The number of branches in the anterior communicating artery.
        Total (MorphologicalFeatures): The total morphological features.
        ACA (MorphologicalFeatures): The morphological features of the anterior cerebral artery.
        PCA (MorphologicalFeatures): The morphological features of the posterior cerebral artery.
        MCA (MorphologicalFeatures): The morphological features of the middle cerebral artery.
    """
    length: float
    branch_number: int
    L_length: float
    L_branch_number: int
    proximal_L_length: float
    proximal_L_branch_number: int
    distal_L_length: float
    distal_L_branch_number: int
    R_length: float
    R_branch_number :int
    proximal_R_length: float
    proximal_R_branch_number: int
    distal_R_length: float
    distal_R_branch_number: int
    proximal_length: float
    proximal_branch_number: int
    distal_length: float
    distal_branch_number: int
    PComm_L_length: float
    PComm_L_branch_number: int
    PComm_R_length: float
    PComm_R_branch_number: int
    AComm_length: float
    AComm_branch_number: int

class GraphicalFeatures(BaseModel):
    """
    Represents a set of graphical features of a graph.

    Attributes:
        average_degree (float): The average degree of the nodes in the graph.
        average_clustering_coefficient (float): The average clustering coefficient of the nodes in the graph.
        assortativity (float): The assortativity coefficient of the graph.
        average_betweenness_centrality (float): The average betweenness centrality of the nodes in the graph.
        average_closeness_centrality (float): The average closeness centrality of the nodes in the graph.
        average_pagerank (float): The average PageRank score of the nodes in the graph.
        average_degree_centrality (float): The average degree centrality of the nodes in the graph.
        average_edge_betweenness_centrality (float): The average edge betweenness centrality of the edges in the graph.
    """
    average_degree: float
    average_clustering_coefficient: float
    assortativity: float
    average_betweenness_centrality: float
    average_closeness_centrality: float
    average_pagerank: float
    average_degree_centrality: float
    average_edge_betweenness_centrality: float


class Subject(SQLModel, table=True):
    """
    Represents a subject in the study.

    Attributes:
        ID (str): The unique identifier for the subject.
        Age (int): The age of the subject.
        Smoking (bool): Indicates whether the subject is a smoker or not.
        SBP (float): The systolic blood pressure of the subject.
        DBP (float): The diastolic blood pressure of the subject.
        Hypertension (bool): Indicates whether the subject has hypertension or not.
        TC (float): The total cholesterol level of the subject.
        TG (float): The triglyceride level of the subject.
        HDL (float): The high-density lipoprotein (HDL) cholesterol level of the subject.
        LDL (float): The low-density lipoprotein (LDL) cholesterol level of the subject.
        Diabetes (bool): Indicates whether the subject has diabetes or not.
        Framingham_Risk (float): The Framingham Risk Score of the subject.
        Gender (Gender): The gender of the subject.
        Race (Race): The race of the subject.
        unstructured_data (Optional[str]): unstructured brain artery network data extracted from .swc file for the subject.
        morphological_features (Optional[str]): Additional morphological features for the subject.
    """
    __tablename__ = "subjects"
    __table_args__ = {'extend_existing': True} 

    ID: str = Field(default="", primary_key=True)
    Age: int
    Smoking: bool
    SBP: float
    DBP: float
    Hypertension: bool
    TC: float
    TG: float
    HDL: float
    LDL: float
    Diabetes: bool
    Framingham_Risk: float
    Gender: Gender
    Race: Race
    unstructured_data: Optional[str]
    morphological_features: Optional[str]


class SubjectRecord(SQLModel):
    """
    Represents a subject in the study.

    Attributes:
        ID (str): The unique identifier for the subject.
        Age (int): The age of the subject.
        Smoking (bool): Indicates whether the subject is a smoker or not.
        SBP (float): The systolic blood pressure of the subject.
        DBP (float): The diastolic blood pressure of the subject.
        Hypertension (bool): Indicates whether the subject has hypertension or not.
        TC (float): The total cholesterol level of the subject.
        TG (float): The triglyceride level of the subject.
        HDL (float): The high-density lipoprotein (HDL) cholesterol level of the subject.
        LDL (float): The low-density lipoprotein (LDL) cholesterol level of the subject.
        Diabetes (bool): Indicates whether the subject has diabetes or not.
        Framingham_Risk (float): The Framingham Risk Score of the subject.
        Gender (Gender): The gender of the subject.
        Race (Race): The race of the subject.
    """
    ID: str
    Age: int
    Smoking: bool
    SBP: float
    DBP: float
    Hypertension: bool
    TC: float
    TG: float
    HDL: float
    LDL: float
    Diabetes: bool
    Framingham_Risk: float
    Gender: Gender
    Race: Race

class MetadataDB(BaseModel):
    """
    Represents a subject in the study.

    Attributes:
        Age (int): The age of the subject.
        SBP (float): The systolic blood pressure of the subject.
        DBP (float): The diastolic blood pressure of the subject.
        TC (float): The total cholesterol level of the subject.
        TG (float): The triglyceride level of the subject.
        HDL (float): The high-density lipoprotein (HDL) cholesterol level of the subject.
        LDL (float): The low-density lipoprotein (LDL) cholesterol level of the subject.
        Framingham_Risk (float): The Framingham Risk Score of the subject.
    """
    age : Optional[Info]
    sbp: Optional[Info]
    dbp: Optional[Info]
    tc: Optional[Info]
    tg: Optional[Info]
    hdl: Optional[Info]
    ldl: Optional[Info]
    framingham_risk: Optional[Info]


class FilterDB(BaseModel):
    """
    Represents a subject in the study.

    Attributes:
        ID (str): The unique identifier for the subject.
        Age (int): The age of the subject.
        Smoking (bool): Indicates whether the subject is a smoker or not.
        SBP (float): The systolic blood pressure of the subject.
        DBP (float): The diastolic blood pressure of the subject.
        Hypertension (bool): Indicates whether the subject has hypertension or not.
        TC (float): The total cholesterol level of the subject.
        TG (float): The triglyceride level of the subject.
        HDL (float): The high-density lipoprotein (HDL) cholesterol level of the subject.
        LDL (float): The low-density lipoprotein (LDL) cholesterol level of the subject.
        Diabetes (bool): Indicates whether the subject has diabetes or not.
        Framingham_Risk (float): The Framingham Risk Score of the subject.
        Gender (Gender): The gender of the subject.
        Race (Race): The race of the subject.
    """
    ID: Optional[List[str]] = []
    datasets: Optional[List[str]] = []
    age: Optional[Tuple] = tuple()
    smoking: Optional[bool]
    sbp: Optional[Tuple] = tuple()
    dbp: Optional[Tuple] = tuple()
    hypertension: Optional[bool]
    tc: Optional[Tuple] = tuple()
    tg: Optional[Tuple] = tuple()
    hdl: Optional[Tuple] = tuple()
    ldl: Optional[Tuple] = tuple()
    diabetes: Optional[bool]
    framingham_risk: Optional[Tuple] = tuple()
    genders: Optional[List[Gender]] = [gender for gender in Gender]
    races: Optional[List[Race]] = [race for race in Race]