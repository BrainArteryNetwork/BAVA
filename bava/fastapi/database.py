
"""SQL Database models for each subject"""

from typing import Optional, List

from sqlmodel import Field, SQLModel, or_, text
from config import SQL_TABlE_NAME
from schemas import Gender, Race


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
    return statement.where(Subject.Age >= min, Subject.Age < max)

def filter_smoking(statement, is_smoking: bool):
    return statement.where(Subject.Smoking == is_smoking)

def filter_sbp(statement, min: float, max: float):
    return statement.where(Subject.SBP >= min, Subject.SBP < max)

def filter_dbp(statement, min: float, max: float):
    return statement.where(Subject.DBP >= min, Subject.DBP < max)

def filter_hypertension(statement, is_hypertension: bool):
    return statement.where(Subject.Hypertension == is_hypertension)

def filter_tc(statement, min: float, max: float):
    return statement.where(Subject.TC >= min, Subject.TC < max)

def filter_tg(statement, min: float, max: float):
    return statement.where(Subject.TG >= min, Subject.TG < max)

def filter_hdl(statement, min: float, max: float):
    return statement.where(Subject.HDL >= min, Subject.HDL < max)

def filter_ldl(statement, min: float, max: float):
    return statement.where(Subject.LDL >= min, Subject.LDL < max)

def filter_diabetes(statement, is_diabetes: bool):
    return statement.where(Subject.Hypertension == is_diabetes)

def filter_framingham_risk(statement, min: float, max: float):
    return statement.where(Subject.Framingham_Risk >= min, Subject.Framingham_Risk < max)

def filter_gender(statement, genders: List[Gender]):
    gender_conditions = []
    for gender in genders:
        gender_conditions.append(f"{SQL_TABlE_NAME}.Gender == \'{gender.name}\'")
    sql_or_statement = text("(" + " OR ".join(gender_conditions) + ")")
    return statement.where(or_(sql_or_statement))

def filter_race(statement, races: List[Race]):
    race_conditions = []
    for race in races:
        race_conditions.append(f"{SQL_TABlE_NAME}.Race == \'{race.name}\'")
    sql_or_statement = text("(" + " OR ".join(race_conditions) + ")")
    return statement.where(or_(sql_or_statement))
