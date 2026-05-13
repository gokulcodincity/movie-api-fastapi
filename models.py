from pydantic import BaseModel, Field

class Movie(BaseModel):
    title:str = Field(..., min_length=1)
    genre: str
    rating: float
    