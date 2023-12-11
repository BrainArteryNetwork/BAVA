
"""SQL Database models for each subject"""

from typing import List

from sqlmodel import or_, text, Session, select
from .config import SQL_TABLE_NAME
from .schemas import Gender, Race, Info, Subject, MetadataDB

class BavaDB:
    subjects: List[Subject] = []
    metadata: MetadataDB = MetadataDB()
    db_session: Session = None

    def __init__(self, db_session: Session=None, subjects=[], metadata=None) -> None:

        if subjects and metadata:
            self.subjects = subjects
            self.metadata = MetadataDB(**metadata)

        elif db_session:
            self.db_session = db_session
            self.subjects = self.db_session.exec(select(Subject)).all()
            self.create_metadata_db()
        
        else:
            raise NotImplementedError
    
    def create_metadata_db(self):
        self.metadata.age = self.get_column_info ("Age")
        self.metadata.sbp = self.get_column_info("SBP")
        self.metadata.dbp = self.get_column_info("DBP")
        self.metadata.tc = self.get_column_info("TC")
        self.metadata.tg = self.get_column_info("TG")
        self.metadata.hdl = self.get_column_info("HDL")
        self.metadata.ldl = self.get_column_info("LDL")
        self.metadata.framingham_risk = self.get_column_info("Framingham_Risk")

    def get_column_info(self, column: str):
        info = Info()
        info.min = self.db_session.exec(text(f"SELECT MIN({column}) FROM {SQL_TABLE_NAME}")).all()[0][0]
        info.max = self.db_session.exec(text(f"SELECT MAX({column}) FROM {SQL_TABLE_NAME}")).all()[0][0]
        info.avg = self.db_session.exec(text(f"SELECT AVG({column}) FROM {SQL_TABLE_NAME}")).all()[0][0]
        return info
    
    def to_dict(self):
        return {
            "subjects": self.subjects,
            "metadata": self.metadata
        }
    
    @classmethod
    def from_dict(cls, db_dict: dict):
        return cls(**db_dict)
    

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
    return statement.where(Subject.Diabetes == is_diabetes)

def filter_framingham_risk(statement, min: float, max: float):
    return statement.where(Subject.Framingham_Risk >= min, 
                           Subject.Framingham_Risk < max)

def filter_gender(statement, genders: List[Gender]):
    gender_conditions = []
    for gender in genders:
        gender_conditions.append(f"{SQL_TABLE_NAME}.Gender == \'{gender.name}\'")
    sql_or_statement = text("(" + " OR ".join(gender_conditions) + ")")
    return statement.where(or_(sql_or_statement))

def filter_race(statement, races: List[Race]):
    race_conditions = []
    for race in races:
        race_conditions.append(f"{SQL_TABLE_NAME}.Race == \'{race.name}\'")
    sql_or_statement = text("(" + " OR ".join(race_conditions) + ")")
    return statement.where(or_(sql_or_statement))
