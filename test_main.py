
import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()


# Get all posts
@app.get("/posts")
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    return response.json()


# Get first two posts
@app.get("/posts/first-two")
def get_first_two_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    data = response.json()

    return data[:2]


# Get a particular post using post_id
@app.get("/posts/{post_id}")
def get_post(post_id: int):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    return response.json()


