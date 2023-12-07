"""Pydantic module for patient DB"""

from enum import Enum
from typing import Optional
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


class Patient(SQLModel, table=True):
    """
    """
    ID: str = Field(default="", primary_key=True)
    Age: int
    Smoking: bool
    SBP: float
    DBP: float
    Hypertension: int
    TC: float
    TG: float
    HDL: float
    LDL: float
    Diabetes: int
    Framingham_Risk: float
    Gender: Gender
    Race: Race
    unstructured_data: Optional[bytes]