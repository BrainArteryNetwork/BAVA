""""""
from typing import List
from fastapi import FastAPI, HTTPException
from sqlmodel import Session, SQLModel, select

from database import Subject, SubjectRecord, SubjectData, filter_age, filter_race, filter_gender, filter_diabetes
from config import create_sql_engine
from schemas import FilterDB

app = FastAPI()
engine = create_sql_engine()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/subjects/", response_model=List[SubjectRecord])
async def get_all_subjects():
    with Session(engine) as session:
        subjects = session.exec(select(Subject)).all()
        return subjects
    
@app.get("/subject", response_model=SubjectData)
async def get_subject_data(subject_id: str):
    with Session(engine) as session:
        subject = session.get(Subject, subject_id)
        if not subject:
            raise HTTPException(status_code=404, detail="Subject data not found")        
        return subject

@app.post("/filter/", response_model=List[SubjectRecord])
async def get_filtered_data(filter_options: FilterDB):
    with Session(engine) as session:
        statement = select(Subject)
        statement = filter_age(statement, filter_options.age[0], filter_options.age[1])
        statement = filter_diabetes(statement, filter_options.diabetes)
        statement = filter_gender(statement, filter_options.genders)
        statement = filter_race(statement, filter_options.races)
        results = session.exec(statement).all()
        return results
