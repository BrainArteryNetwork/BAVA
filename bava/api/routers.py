"""
This module provides a FastAPI application for interacting with the BAVA database.

The following endpoints are available:

    - GET /subjects/ - Retrieves all subjects from the database.
    - GET /subjects/{subject_id} - Retrieves a subject by its ID.
    - POST /filter/ - Retrieves filtered data from the database.

The module also defines a helper function for creating a new SQLAlchemy session with the database engine.

Attributes:
    app (FastAPI): A FastAPI application object.
    engine (Engine): A SQLModel engine object for connecting to the database.
"""
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
    """
    A helper function to create a new session with the database engine.

    Returns:
        A new SQLModel Session object.
    """
    with Session(engine) as session:
        yield session

@app.on_event("startup")
def on_startup():
    """
    A function to create the database tables when the application starts up.
    """
    SQLModel.metadata.create_all(engine)

@app.get("/subjects/", response_model=Dict)
async def get_all_subjects(session: Session = Depends(get_session)):
    """
    A function to retrieve all subjects from the database.

    Args:
        session (Session): A SQLModel Session object.

    Returns:
        A dictionary containing all subjects in the database along with metadata.
    """
    bava_database = BavaDB(session)
    return bava_database.to_dict()

@app.get("/subjects/{subject_id}", response_model=Subject)
async def get_by_subject_id(*, session: Session = Depends(get_session), subject_id: str):
    """
    A function to retrieve a subject by its ID.

    Args:
        session (Session): A SQLModel Session object.
        subject_id (str): The ID of the subject to retrieve.

    Returns:
        The subject with the specified ID.

    Raises:
        HTTPException: If no subject with the specified ID is found.
    """
    subject = session.get(Subject, subject_id)
    if not subject:
        raise HTTPException(status_code=404, detail=f"Subject with id:{subject_id} not found")
    return subject

@app.post("/filter/", response_model=List[SubjectRecord])
async def get_filtered_data(*, session: Session = Depends(get_session), filter_options: FilterDB):
    """
    A function to retrieve filtered data from the database.

    Args:
        session (Session): A SQLModel Session object.
        filter_options (FilterDB): A FilterDB object containing the filter options.

    Returns:
        A list of SubjectRecord objects that match the specified filters.
    """
    statement = select(Subject)
    statement = filter_age(statement, filter_options.age[0], filter_options.age[1])
    statement = filter_diabetes(statement, filter_options.diabetes)
    statement = filter_gender(statement, filter_options.genders)
    statement = filter_race(statement, filter_options.races)
    results = session.exec(statement).all()
    return results
