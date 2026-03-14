from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "postgresql://postgres:Shakthi%40777@localhost/moviereviews"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind = engine)

Base = declarative_base()