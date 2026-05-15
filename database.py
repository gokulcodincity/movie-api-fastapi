from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongodb_url = os.getenv("MONGO_URL")

mongodb_client = MongoClient(mongodb_url)

movie_database = mongodb_client.movie_database

movies_collection = movie_database.movies