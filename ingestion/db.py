from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from ingestion.config import DATABASE_URL


def get_engine() -> Engine:
    """
    Create and return a SQLAlchemy engine for the Neon PostgreSQL database.
    """
    return create_engine(
        DATABASE_URL,
        pool_pre_ping=True,
        future=True,
    )