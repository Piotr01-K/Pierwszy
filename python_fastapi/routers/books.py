from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

# tworzymy router dla książek
router = APIRouter(
    prefix="/books",
    tags=["Books"]  # pojawi się w Swaggerze jako sekcja
)

# -------- MODEL --------
class Book(BaseModel):
    title: str
    author: str


# -------- "BAZA DANYCH" W PAMIĘCI --------
books_db = {}
next_book_id = 1


# GET /books
@router.get("/")
async def get_books():
    """Zwraca listę wszystkich książek"""
    return books_db


# GET /books/{id}
@router.get("/{book_id}")
async def get_book(book_id: int):
    """Zwraca jedną książkę po ID"""
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[book_id]


# POST /books
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    """Dodaje nową książkę"""
    global next_book_id

    books_db[next_book_id] = book
    next_book_id += 1

    return book


# DELETE /books/{id}
@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    """Usuwa książkę"""
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")

    del books_db[book_id]