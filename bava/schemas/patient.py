"""Pydantic module for patient DB"""

from typing import Optional
from sqlmodel import Field, SQLModel

class Patient(SQLModel, table=True):
    """
    """
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
    Gender: int
    Race: int