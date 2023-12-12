""""""
from enum import Enum
from typing import Optional, List, Tuple
from pydantic import BaseModel

from sqlmodel import Field, SQLModel

class Gender(Enum):
    """
    """
    female = 0
    male = 1


class Race(Enum):
    """
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

class Subject(SQLModel, table=True):
    """
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

class SubjectRecord(SQLModel):
    """
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