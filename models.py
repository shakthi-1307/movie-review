from sqlalchemy import Column,Integer,String,Text,TIMESTAMP
from database import Base
from sqlalchemy.sql import func

class Review(Base):
    __tablename__ = 'reviews'
    
    id = Column(Integer,primary_key = True,index = True)
    movie = Column(String)
    rating = Column(Integer)
    review = Column(Text)
    created_at = Column(TIMESTAMP,server_default = func.now())
    
    