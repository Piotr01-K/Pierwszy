# task13 api gateway
from fastapi import FastAPI
import httpx

app = FastAPI(title="API Gateway")

USERS_URL = "http://users-service:8000/users"
POSTS_URL = "http://posts-service:8000/posts"

@app.get("/aggregate")
async def aggregate():
    async with httpx.AsyncClient() as client:
        users = await client.get(USERS_URL)
        posts = await client.get(POSTS_URL)

    return {
        "users": users.json(),
        "posts": posts.json()
    }