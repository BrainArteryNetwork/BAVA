from typing import Optional, List, Tuple
from pydantic import BaseModel

from database import Gender, Race

class FilterDB(BaseModel):
    ID: Optional[List[str]]
    age: Optional[Tuple]
    smoking: Optional[bool]
    sbp: Optional[Tuple]
    dbp: Optional[Tuple]
    hypertension: Optional[bool]
    tc: Optional[Tuple]
    tg: Optional[Tuple]
    hdl: Optional[Tuple]
    ldl: Optional[Tuple]
    diabetes: Optional[bool]
    framingham_risk: Optional[Tuple]
    gender: Optional[List[Gender]]
    race: Optional[List[Race]]