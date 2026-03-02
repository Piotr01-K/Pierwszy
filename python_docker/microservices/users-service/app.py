# task13 users service

import asyncio
from fastapi import FastAPI
import asyncpg
import os

app = FastAPI(title="Users Service")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@users-db:5432/usersdb"
)

@app.on_event("startup")
async def startup():
    print("Connecting to users database...")

    for attempt in range(10):
        try:
            app.state.pool = await asyncpg.create_pool(DATABASE_URL)

            async with app.state.pool.acquire() as conn:
                await conn.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        name TEXT
                    )
                """)
            print("✅ Users DB connected")
            return

        except Exception:
            print(f"Users DB not ready (attempt {attempt+1})...")
            await asyncio.sleep(2)

    raise Exception("❌ Could not connect to users database")

@app.get("/users")
async def get_users():
    async with app.state.pool.acquire() as conn:
        rows = await conn.fetch("SELECT * FROM users")
        return [dict(r) for r in rows]