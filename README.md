# Techie Blog API

This is a Django-based API for managing a blog application called  Techie. It provides endpoints for creating, retrieving, updating, and deleting blog posts.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.8 or higher
- Django 4.2.2 or higher
- Django REST Framework 3.12.4 or higher

## Installation

1. Clone the repository:

`git clone https://github.com/aglili/techie_trial.git`

2. Navigate to the project directory:

`cd techie_trial`


3. Create a virtual environment:

`virtualenv venv`


4. Activate the virtual environment:

   On macOS and Linux:

`source env/bin/activate`


   On Windows:

`venv/scripts/activate`


5. Install the dependencies:

`pip install -r requirements.txt`



## Usage

1. Start the development server:

`python manage.py runserver`


2. Access the API at `http://localhost:8000/`


3. Use a tool like Postman to interact with the API endpoints. See the available endpoints below.

## API Endpoints


- **POST** `signup`: create a new user.
- **POST** `login`: login with user details to get access token.
- **GET** `blogs/public`: Get all posts without login or signup.
- **POST** `blog`: Create a new blog post.
- **GET** `blog/all`: Get all an authenticated users posts.
- **PATCH** `blog/update`: Update a specific blog post.
- **DELETE** `blog/delete`: Delete all a specific users  blog posts.



## Authentication

The API uses JSON Web Token (JWT) authentication. To access protected endpoints, you need to include an access token in the request header.

To obtain an access token, you can use the `/login` endpoint with your username and password. The response will include an access token that you can use for subsequent requests.

Example request:
```json
{
"username": "your-username",
"password": "your-password"
}


{
    "access": "your-access-token",
    "refresh": "your-refresh-token"
}

To authenticate subsequent requests, include the access token in the Authorization header:

`Authorization: Bearer your-access-token`





