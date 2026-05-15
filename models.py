from pydantic import BaseModel, Field


class MovieData(BaseModel):
    title: str = Field(..., min_length=1)
    genre: str
    rating: float