from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do bazy danych (na razie SQLite lokalnie)
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# Tworzenie async engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # pokazuje zapytania SQL w konsoli
    future=True
)

# Session factory - tworzy nowe sesje DB
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

# Base class dla modeli ORM
Base = declarative_base()

# Dependency injection dla sesji bazy
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

# Funkcja tworząca tabele przy starcie aplikacji
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# dodane lesson 33 task 13
DATABASE_URL = "sqlite+aiosqlite:///./books.db"

# async engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # pokazuje SQL w terminalu (nauka!)
)

# fabryka sesji
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# baza dla modeli ORM
Base = declarative_base()


# dependency do FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


# tworzenie tabel
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)