# task 10 fastapi_crud_books

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncpg
import os
import asyncio

DATABASE_URL = "postgresql://postgres:postgres@database:5432/mydb"

app = FastAPI()


class BookIn(BaseModel):
    title: str
    author: str


@app.on_event("startup")
async def startup():
    print("Connecting to database...")

    # 🔁 retry loop
    for attempt in range(10):
        try:
            app.state.pool = await asyncpg.create_pool(DATABASE_URL)
            print("✅ Connected to PostgreSQL")
            break
        except Exception as e:
            print(f"Database not ready (attempt {attempt + 1})...")
            await asyncio.sleep(2)
    else:
        raise Exception("❌ Could not connect to database")

    async with app.state.pool.acquire() as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id SERIAL PRIMARY KEY,
                title TEXT,
                author TEXT
            )
        """)

@app.get("/books")
async def list_books():
    async with app.state.pool.acquire() as conn:
        rows = await conn.fetch("SELECT * FROM books")
    return [dict(r) for r in rows]


@app.post("/books")
async def create_book(book: BookIn):
    async with app.state.pool.acquire() as conn:
        row = await conn.fetchrow(
            "INSERT INTO books (title, author) VALUES ($1, $2) RETURNING *",
            book.title,
            book.author
        )
    return dict(row)


@app.put("/books/{book_id}")
async def update_book(book_id: int, book: BookIn):
    async with app.state.pool.acquire() as conn:
        row = await conn.fetchrow(
            "UPDATE books SET title=$1, author=$2 WHERE id=$3 RETURNING *",
            book.title,
            book.author,
            book_id
        )
    if not row:
        raise HTTPException(status_code=404, detail="Book not found")
    return dict(row)


@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    async with app.state.pool.acquire() as conn:
        result = await conn.execute(
            "DELETE FROM books WHERE id=$1",
            book_id
        )
    return {"status": result}