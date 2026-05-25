from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


DATABASE_URL = ("postgresql://postgres:nimap@localhost:5432/creator")

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind=engine,
)

Base = declarative_base()