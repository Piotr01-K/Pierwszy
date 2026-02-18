from fastapi import APIRouter, Depends
from pydantic import BaseModel
from dependencies import verify_api_key

router = APIRouter(
    prefix="/authors",
    tags=["Authors"]
)

class Author(BaseModel):
    name: str


authors_db = {}
next_author_id = 1


@router.get("/")
async def get_authors():
    """Lista autorów"""
    return authors_db


@router.post("/")
async def create_author(author: Author):
    """Dodaje autora"""
    global next_author_id
    authors_db[next_author_id] = author
    next_author_id += 1
    return author