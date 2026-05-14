from fastapi import FastAPI, HTTPException
from bson import ObjectId

from models import MovieData
from database import movies_collection

app = FastAPI()


@app.post("/insert-movies")
def create_movie(movie_data: MovieData):

    new_movie = movie_data.dict()

    inserted_movie = movies_collection.insert_one(new_movie)

    created_movie = movies_collection.find_one(
        {"_id": inserted_movie.inserted_id}
    )

    created_movie["_id"] = str(created_movie["_id"])

    return {
        "message": "Movie created successfully",
        "movie": created_movie
    }


@app.get("/movies/{movie_id}")
def get_movie(movie_id: str):

    if not ObjectId.is_valid(movie_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid movie ID"
        )

    found_movie = movies_collection.find_one(
        {"_id": ObjectId(movie_id)}
    )

    if not found_movie:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    found_movie["_id"] = str(found_movie["_id"])

    return {
        "message": "Movie fetched successfully",
        "movie": found_movie
    }
@app.get("/movies")
def get_all_movies():

    all_movies = []

    for movie in movies_collection.find():

        movie["_id"] = str(movie["_id"])

        all_movies.append(movie)

    return {
        "movies": all_movies
    }