from fastapi import APIRouter
from pydantic import BaseModel

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