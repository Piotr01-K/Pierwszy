# routers/books.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from models import BookORM
from schemas import BookCreate, BookResponse
from dependencies import verify_api_key

router = APIRouter(
    prefix="/books",
    tags=["Books"],
    dependencies=[Depends(verify_api_key)]
)


# ================================
# GET /books — lista książek
# ================================
@router.get("/", response_model=list[BookResponse])
async def get_books(db: AsyncSession = Depends(get_db)):
    # pobieramy wszystkie książki z bazy
    result = await db.execute(select(BookORM))
    books = result.scalars().all()
    return books


# ================================
# GET /books/{id}
# ================================
@router.get("/{book_id}", response_model=BookResponse)
async def get_book(book_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(BookORM).where(BookORM.id == book_id)
    )
    book = result.scalar_one_or_none()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


# ================================
# POST /books
# ================================
@router.post("/", response_model=BookResponse, status_code=201)
async def create_book(
    book: BookCreate,
    db: AsyncSession = Depends(get_db)
):
    db_book = BookORM(**book.model_dump())

    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)

    return db_book


# ================================
# DELETE /books/{id}
# ================================
@router.delete("/{book_id}", status_code=204)
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(BookORM).where(BookORM.id == book_id)
    )
    book = result.scalar_one_or_none()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    await db.delete(book)
    await db.commit()

    return None