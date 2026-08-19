from sqlalchemy import creeate_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import sessionmaker

DATABSE_URL = "postgresql://postgres:postgres@localhost/escola"

engine = creeate_engine(DATABSE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
