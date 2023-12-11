""""""
from typing import List, Dict
from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, SQLModel, select

from .database import (filter_age, filter_race, 
                      filter_gender, filter_diabetes, BavaDB)
from .config import create_sql_engine
from .schemas import FilterDB, Subject, SubjectRecord

app = FastAPI(title="BAVA API",
              description="API to get subject information for BAVA DB",
              version="1.0.0")

engine = create_sql_engine()

async def get_session():
    with Session(engine) as session:
        yield session

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/subjects/", response_model=Dict)
async def get_all_subjects(session: Session = Depends(get_session)):
    bava_database = BavaDB(session)
    return bava_database.to_dict()

@app.get("/subjects/{subject_id}", response_model=Subject)
async def get_by_subject_id(*, session: Session = Depends(get_session), subject_id: str):
    subject = session.get(Subject, subject_id)
    if not subject:
        raise HTTPException(status_code=404, detail=f"Subject with id:{subject_id} not found")
    return subject

@app.post("/filter/", response_model=List[SubjectRecord])
async def get_filtered_data(*, session: Session = Depends(get_session), filter_options: FilterDB):
    print(filter_options)
    statement = select(Subject)
    statement = filter_age(statement, filter_options.age[0], filter_options.age[1])
    statement = filter_diabetes(statement, filter_options.diabetes)
    statement = filter_gender(statement, filter_options.genders)
    statement = filter_race(statement, filter_options.races)
    results = session.exec(statement).all()
    return results
