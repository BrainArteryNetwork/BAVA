"""
This module contains functions and variables for managing the database.

    FAST_API_URL: A string representing the URL of the FastAPI server.
    SQL_TABLE_NAME: A string representing the name of the SQL table.
    SQL_DB_FILENAME: A string representing the name of the SQL database file.
    SQL_DB_URL: A string representing the URL of the SQL database.

"""
from sqlmodel import create_engine

FAST_API_URL = "http://127.0.0.1:8000"

SQL_TABLE_NAME = "subjects"
SQL_DB_FILENAME = "subjects_all.db"
SQL_DB_URL = f"sqlite:///./data/{SQL_DB_FILENAME}"

def create_sql_engine():
    """
    Creates a new SQLModel engine for the database.

    Returns:
    Engine: A new SQLModel engine object.
    """
    connect_args = {"check_same_thread": False}
    engine = create_engine(SQL_DB_URL, echo=True, connect_args=connect_args)
    return engine