from fastapi import APIRouter, HTTPException
from bson import ObjectId

from app.models import Movie
from app.database import movies_collection

router = APIRouter()
@router.get("/")
def home():
    return {
        "message":"API Working Corectly"
    }

# CREATE MOVIE
@router.post("/movies", status_code=201)
def create_movie(movie: Movie):

    new_movie = movie.dict()

    result = movies_collection.insert_one(new_movie)

    created_movie = movies_collection.find_one(
        {"_id": result.inserted_id}
    )

    created_movie["_id"] = str(created_movie["_id"])

    return {
        "message": "Movie created successfully",
        "movie": created_movie
    }


# GET MOVIE BY ID
@router.get("/movies/{movie_id}", status_code=200)
def get_movie(movie_id: str):

    if not ObjectId.is_valid(movie_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid movie ID"
        )

    movie = movies_collection.find_one(
        {"_id": ObjectId(movie_id)}
    )

    if not movie:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    movie["_id"] = str(movie["_id"])

    language_count = len(movie["languages"])

    if movie["rating"] >= 8:
        review = "Excellent movie"

    elif movie["rating"] >= 5:
        review = "Good movie"

    else:
        review = "Average movie"

    return {
        "title": movie["title"],
        "genre": movie["genre"],
        "rating": movie["rating"],
        "release_year": movie["release_year"],
        "number_of_languages": language_count,
        "review_message": review
    }


# FILTER MOVIES BY GENRE
@router.get("/movies")
def filter_movies(genre: str = None,
                  title: str =None,
                  rating: float = None,
                  release_year: int = None
                  ):

    query = {}

    if genre:
        query["genre"] = genre

    if title:
        query["title"] = title

    if rating:
        query["rating"] = rating

    if release_year:
        query["release_year"] = release_year


    movies = []

    for movie in movies_collection.find(query):

        movie["_id"] = str(movie["_id"])

        movies.append(movie)

    return {
        "movies": movies
    }