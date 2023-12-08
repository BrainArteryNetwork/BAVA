""""""
from typing import List
from fastapi import FastAPI, Response
from sqlmodel import Field, Session, SQLModel, create_engine, select

from database import Subject, SubjectRecord

sqlite_file_name = "subjects4.db"
sqlite_url = f"sqlite:///../../data/{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    """
    """
    SQLModel.metadata.create_all(engine)


app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/subjects/", response_model=List[SubjectRecord])
async def read_subjects():
    with Session(engine) as session:
        subjects = session.exec(select(Subject)).all()
        return subjects