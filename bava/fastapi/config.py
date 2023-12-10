"""
"""
from sqlmodel import create_engine

SQL_TABlE_NAME = "subjects"
SQL_DB_FILENAME = "subjects.db"
SQL_DB_URL = f"sqlite:///../../data/{SQL_DB_FILENAME}"

def create_sql_engine():
    connect_args = {"check_same_thread": False}
    engine = create_engine(SQL_DB_URL, echo=True, connect_args=connect_args)
    return engine