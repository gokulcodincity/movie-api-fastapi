# Movie Collection API

A beginner-friendly FastAPI capstone project for managing a movie collection using MongoDB Atlas.

This project demonstrates:

* FastAPI basics
* CRUD API development
* MongoDB integration
* Pydantic validation
* Path parameters
* Query parameters
* HTTP status codes
* Exception handling
* Postman and Swagger testing

---

# Technologies Used

| Technology    | Purpose                      |
| ------------- | ---------------------------- |
| Python        | Backend programming language |
| FastAPI       | API framework                |
| MongoDB Atlas | Cloud database               |
| Pydantic      | Data validation              |
| Uvicorn       | ASGI server                  |
| Postman       | API testing                  |

---

# Project Folder Structure

```text
movie_collection_api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── routes.py
│
├── .env
├── .gitignore
├── README.md
└── pyproject.toml
```

---

# Features

This project includes:

* Create movie API
* Get movie by ID API
* Filter movies API
* MongoDB database connection
* Automatic movie ID generation
* Review message based on movie rating
* Query parameter filtering
* Proper exception handling
* Clean JSON responses

---

# Movie Fields

Each movie contains:

| Field        | Type    |
| ------------ | ------- |
| title        | string  |
| genre        | string  |
| rating       | float   |
| release_year | integer |
| languages    | list    |

Example:

```json
{
  "title": "Leo",
  "genre": "Action",
  "rating": 8.5,
  "release_year": 2023,
  "languages": ["Tamil", "English"]
}
```

---

# API Endpoints

## 1. Create Movie

### Endpoint

```text
POST /movies
```

### Description

Creates and stores a new movie in MongoDB.

### Request Body

```json
{
  "title": "Leo",
  "genre": "Action",
  "rating": 8.5,
  "release_year": 2023,
  "languages": ["Tamil", "English"]
}
```

### Success Response

```json
{
  "message": "Movie created successfully",
  "movie": {
    "_id": "682123abc123",
    "title": "Leo",
    "genre": "Action",
    "rating": 8.5,
    "release_year": 2023,
    "languages": ["Tamil", "English"]
  }
}
```

### Status Code

```text
201 Created
```

---

# 2. Get Movie By ID

### Endpoint

```text
GET /movies/{movie_id}
```

### Description

Fetches a single movie using MongoDB ObjectId.

### Example

```text
GET /movies/682123abc123
```

### Response

```json
{
  "title": "Leo",
  "genre": "Action",
  "rating": 8.5,
  "release_year": 2023,
  "number_of_languages": 2,
  "review_message": "Excellent movie"
}
```

---

# Review Message Conditions

| Rating      | Review Message  |
| ----------- | --------------- |
| rating >= 8 | Excellent movie |
| rating >= 5 | Good movie      |
| rating < 5  | Average movie   |

---

# 3. Filter Movies Using Query Parameters

### Endpoint

```text
GET /movies
```

### Supported Filters

| Query Parameter | Example                   |
| --------------- | ------------------------- |
| title           | /movies?title=Leo         |
| genre           | /movies?genre=Action      |
| rating          | /movies?rating=8.5        |
| release_year    | /movies?release_year=2023 |

---

# Multiple Filters Example

```text
/movies?genre=Action&rating=8.5
```

### Response

```json
{
  "movies": [
    {
      "title": "Leo",
      "genre": "Action",
      "rating": 8.5,
      "release_year": 2023,
      "languages": ["Tamil", "English"]
    }
  ]
}
```

---

# Exception Handling

The project uses FastAPI HTTPException for proper error handling.

### Invalid Movie ID

```json
{
  "detail": "Invalid movie ID"
}
```

### Movie Not Found

```json
{
  "detail": "Movie not found"
}
```

---

# Status Codes Used

| Status Code | Meaning              |
| ----------- | -------------------- |
| 200         | Success              |
| 201         | Created Successfully |
| 400         | Bad Request          |
| 404         | Resource Not Found   |

---

# MongoDB Connection

The project uses MongoDB Atlas cloud database.

Connection string is stored securely using a `.env` file.

Example:

```env
MONGO_URL=your_mongodb_connection_string
```

---

# Installation Steps

## 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPO_LINK
```

---

## 2. Open Project

```bash
cd movie_collection_api
```

---

## 3. Create Virtual Environment

```bash
uv venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

---

## 5. Install Dependencies

```bash
uv add fastapi uvicorn pymongo python-dotenv pydantic
```

---

## 6. Run Project

```bash
uvicorn app.main:app --reload
```

---

# Swagger Documentation

FastAPI automatically provides Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

---

# Postman Testing

This project was tested using Postman.

Tested:

* POST requests
* GET requests
* Query parameter filtering
* Invalid ID handling
* Error responses

---

# Key Concepts Learned

Through this project, I learned:

* FastAPI basics
* API request and response flow
* CRUD operations
* MongoDB integration
* Query parameters
* Path parameters
* HTTP status codes
* Exception handling
* Clean project structure
* Postman testing
* Swagger documentation

---

# Conclusion

This Movie Collection API project helped me understand the fundamentals of backend API development using FastAPI and MongoDB.

I learned how APIs work, how databases are connected, how requests and responses are handled, and how to build clean and structured backend applications.

This project also improved my understanding of debugging, exception handling, and API testing.
