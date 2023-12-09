
"""SQL Database models for each subject"""

from io import BytesIO
from enum import Enum
from typing import Optional

import numpy as np
from sqlmodel import Field, SQLModel, select

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

class SubjectData(SQLModel):
    """
    """
    ID: str
    unstructured_data: Optional[str]


def filter_age(statement, min: int, max: int):
    return statement.where(Subject.Age >= min).where(Subject.Age < max)

def filter_smoking(statement, is_smoking: bool):
    return statement.where(Subject.Smoking == is_smoking)

def filter_sbp(statement, min: float, max: float):
    return statement.where(Subject.SBP >= min).where(Subject.SBP < max)

def filter_dbp(statement, min: float, max: float):
    return statement.where(Subject.DBP >= min).where(Subject.DBP < max)

def filter_hypertension(statement, is_hypertension: bool):
    return statement.where(Subject.Hypertension == is_hypertension)

def filter_tc(statement, min: float, max: float):
    return statement.where(Subject.TC >= min).where(Subject.TC < max)

def filter_tg(statement, min: float, max: float):
    return statement.where(Subject.TG >= min).where(Subject.TG < max)

def filter_hdl(statement, min: float, max: float):
    return statement.where(Subject.HDL >= min).where(Subject.HDL < max)

def filter_ldl(statement, min: float, max: float):
    return statement.where(Subject.LDL >= min).where(Subject.LDL < max)

def filter_diabetes(statement, is_diabetes: bool):
    return statement.where(Subject.Hypertension == is_diabetes)

def filter_framingham_risk(statement, min: float, max: float):
    return statement.where(Subject.Framingham_Risk >= min).where(Subject.Framingham_Risk < max)