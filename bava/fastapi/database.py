
"""SQL Database models for each subject"""

from io import BytesIO
from enum import Enum
from typing import Optional

import numpy as np
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


class Subject(SQLModel, table=True):
    """
    """
    __tablename__ = "subjects"

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
    unstructured_data: Optional[bytes]


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