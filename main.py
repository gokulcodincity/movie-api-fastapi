from fastapi import FastAPI
from models import Movie
from database import movie_collection
from bson import ObjectId
from fastapi import HTTPException


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Movie API Running"
    }

@app.post("/movies")
def create_movie(movie: Movie):
    movie_data = movie.dict()
    result = movie_collection.insert_one(movie_data)

    created_movie = movie_collection.find_one({"_id": result.inserted_id})

    created_movie["_id"] = str(created_movie["_id"])

    return {
        "message" : "Movie Created Successfully",
        "movie": created_movie
    }




@app.get("/movies/{movie_id}")
def get_movie(movie_id: str):

    if not ObjectId.is_valid(movie_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid movie ID"
        )

    movie = movie_collection.find_one(
        {"_id": ObjectId(movie_id)}
    )

    if not movie:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    movie["_id"] = str(movie["_id"])

    return {
        "message": "Movie fetched successfully",
        "movie": movie
    }