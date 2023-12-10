""""""
from enum import Enum
from typing import Optional, List, Tuple
from pydantic import BaseModel


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

class FilterDB(BaseModel):
    ID: Optional[List[str]] = []
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