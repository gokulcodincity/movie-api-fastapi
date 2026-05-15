from pydantic import BaseModel
from typing import List


class Movie(BaseModel):

    title: str
    genre: str
    rating: float
    release_year: int
    languages: List[str]