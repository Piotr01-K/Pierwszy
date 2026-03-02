# task13 posts service

import asyncio
from fastapi import FastAPI
import asyncpg
import os

app = FastAPI(title="Posts Service")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@posts-db:5432/postsdb"
)

@app.on_event("startup")
async def startup():
    print("Connecting to posts database...")

    for attempt in range(10):
        try:
            app.state.pool = await asyncpg.create_pool(DATABASE_URL)

            async with app.state.pool.acquire() as conn:
                await conn.execute("""
                    CREATE TABLE IF NOT EXISTS posts (
                        id SERIAL PRIMARY KEY,
                        title TEXT
                    )
                """)
            print("✅ Posts DB connected")
            return

        except Exception:
            print(f"Posts DB not ready (attempt {attempt+1})...")
            await asyncio.sleep(2)

    raise Exception("❌ Could not connect to posts database")

@app.get("/posts")
async def get_posts():
    async with app.state.pool.acquire() as conn:
        rows = await conn.fetch("SELECT * FROM posts")
        return [dict(r) for r in rows]