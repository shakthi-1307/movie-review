from pydantic import BaseModel

class ReviewCreate(BaseModel):
    movie:str
    rating:int
    review:str
    
    