"""
"""
from sqlmodel import create_engine

FAST_API_URL = "http://127.0.0.1:8000"

SQL_TABLE_NAME = "subjects"
SQL_DB_FILENAME = "subjects.db"
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