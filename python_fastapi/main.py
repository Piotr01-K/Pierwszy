from fastapi import FastAPI, Request, Path
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import time
import logging
from fastapi import HTTPException, status, Depends, Header
import asyncio
from datetime import datetime   # dodane Lesson 33 task 1
import random # dodane Lesson 33 task 1
from pydantic import BaseModel, EmailStr  # dodane Lesson 33 task 4, 5
# import routerów
from routers import books, authors  
from dependencies import verify_api_key
from fastapi.openapi.utils import get_openapi
from database import init_db

# API_KEY_NAME = "X-API-Key"
# api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
# api_key_header = APIKeyHeader(name="X-API-Key")

app = FastAPI(
    title="My FastAPI Learning App",
    description="API created during FastAPI course - users, books, products",
    version="1.0.0"
)
# dodane Lesson 33 task 9
app.include_router(books.router)
app.include_router(authors.router)

class AppState:
    db_connection = None
    cache = {}
    background_worker_task = None

app.state = AppState()

# dodane Lesson 33 task 4
class Product(BaseModel):
    name: str
    price: float
    quantity: int

# dodane Lesson 33 task 5
# Model książki (walidacja JSON z requestu)
# class Book(BaseModel):
#     title: str
#     author: str

# dodane Lesson 33 task 7
# ===== MODEL USER =====
class User(BaseModel):
    name: str
    email: EmailStr  # automatyczna walidacja email

# dodane Lesson 33 task 11
class Author(BaseModel):
    name: str
    email: EmailStr  # walidacja email

# ass BookNested(BaseModel):
#   title: str
#   author: Author  # tutaj uwaga: model w modelu!
#   price: float

#  books_db = {}   # Nasza "baza danych" w pamięci (słownik)
#  next_book_id = 1  # licznik ID (auto-increment jak w SQL)

# dodane Lesson 33 task 7
# prosta baza użytkowników w pamięci
users_db = {}
next_user_id = 1

# dodane Lesson 33 task 10
# Dependency sprawdzające API KEY
async def verify_api_key(x_api_key: str = Header(...)):
    """
    Sprawdza czy w nagłówku X-API-Key jest poprawny klucz.
    Header(...) = wymagany nagłówek.
    """

    if x_api_key != "secret-key-123":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
    
# middleware 1 — mierzenie czasu requestu
@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.time()
    logging.info(f"Request started: {request.method} {request.url.path}")

    response = await call_next(request)

    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logging.info(f"Request completed in {process_time:.3f}s")

    return response


# middleware 2 — dodawanie nagłówków
@app.middleware("http")
async def add_custom_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Custom-Header"] = "FastAPI-2024"
    response.headers["X-Request-ID"] = str(id(request))
    return response


# middleware 3 — prosty API KEY
# @app.middleware("http")
# async def verify_api_key(request: Request, call_next):
#     # pozwalamy Swaggerowi działać bez klucza
#    if request.url.path in ["/docs", "/openapi.json", "/redoc"]:
#        return await call_next(request)

#    api_key = request.headers.get(API_KEY_NAME)

#    if api_key != "secret-key-123":
#        from fastapi.responses import JSONResponse
#        return JSONResponse(
#            status_code=401,
#            content={"detail": "Invalid or missing API Key"},
#        )

#    return await call_next(request)


# CORS middleware (dla frontendu)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/test")
async def test_endpoint():
    return {"message": "Hello!"}


async def background_worker():
    try:
        while True:
            logging.info("Background worker: checking for tasks...")
            await asyncio.sleep(60)
    except asyncio.CancelledError:
        logging.info("Background worker cancelled")
        raise

@app.on_event("startup")
async def startup_event():
    logging.info("Application starting up...")

    await init_db()  # tworzy tabele w bazie

    app.state.db_connection = "connected"
    logging.info("Database initialized")

    app.state.cache = {
        "config": {"max_users": 1000},
        "version": "1.0.0"
    }
    logging.info("Cache loaded")

    app.state.background_worker_task = asyncio.create_task(background_worker())
    logging.info("Background worker started")

@app.on_event("shutdown")
async def shutdown_event():
    logging.info("Application shutting down...")

    if app.state.background_worker_task:
        app.state.background_worker_task.cancel()
        try:
            await app.state.background_worker_task
        except asyncio.CancelledError:
            logging.info("Background worker cancelled")

    logging.info("Database connection closed")
    logging.info("Cache saved to disk")

# dodane Lesson 33 task 1, 8
@app.get("/", tags=["General"])
async def root():
    return {"message": "Hello"}

@app.get("/time", tags=["General"])
async def get_time():
    """Returns current server time."""
    from datetime import datetime
    return {"time": datetime.now()}

@app.get("/random", tags=["General"])
async def get_random_number():
    """Returns random number between 1 and 100."""
    import random
    return {"number": random.randint(1, 100)}

# dodane Lesson 33 task 2, 8
@app.get("/greet/{name}", tags=["General"])
async def greet_user(name: str):
    if len(name) < 2:
        raise HTTPException(status_code=400, detail="Name too short")
    return {"message": f"Hello {name}"}

# dodane Lesson 33 task 3, 8
@app.get("/calculate", tags=["Calculator"])
async def calculate(
    a: int,
    b: int,
    operation: str = "add"
):
    """Simple calculator supporting add, subtract, multiply and divide."""
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return {"error": "Division by zero"}
        result = a / b
    else:
        return {"error": "Invalid operation"}

    return {
        "a": a,
        "b": b,
        "operation": operation,
        "result": result
    }

# dodane Lesson 33 task 4, 8
@app.post("/products", tags=["Products"])
async def create_product(product: Product):
    total_price = product.price * product.quantity

    return {
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
        "total_price": total_price
    }
'''''
# dodane Lesson 33 task 5
@app.get("/books", tags=["Books"])
async def get_books(api_key: str = Depends(verify_api_key)):
    return books_db  # zwracamy wszystkie książki jako listę

@app.get("/books/{book_id}", tags=["Books"])
async def get_book(book_id: int, api_key: str = Depends(verify_api_key)):
    # sprawdzamy czy książka istnieje, jak brak do błąd 404
    if book_id not in books_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    return books_db[book_id]

@app.post("/books", tags=["Books"], status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    global next_book_id  # używamy globalnego licznika ID

    # zapisujemy książkę w "bazie"
    books_db[next_book_id] = book

    # przygotowujemy odpowiedź
    response = {
        "id": next_book_id,
        "book": book
    }

    next_book_id += 1  # zwiększamy licznik ID

    return response

@app.delete("/books/{book_id}", tags=["Books"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    # sprawdzamy czy istnieje, jeśli nie błąd 404
    if book_id not in books_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    # usuwamy z "bazy"
    del books_db[book_id]

    return None  # 204 nie zwraca body
'''''
# dodane Lesson 33 task 7
@app.post("/users", tags=["Users"], status_code=status.HTTP_201_CREATED)
async def create_user(user: User, api_key: str = Depends(verify_api_key)):
    global next_user_id

    # zapis do "bazy"
    users_db[next_user_id] = user
    next_user_id += 1

    return user
'''
# dodane Lesson 33 task 11
@app.post("/books/nested", tags=["Nested models"])
async def create_nested_book(book: BookNested):
    """
    Tworzy książkę z zagnieżdżonym autorem.
    """
    
    # przykładowa logika – liczymy cenę z VAT
    price_with_tax = book.price * 1.23
    
    return {
        "title": book.title,
        "author": book.author,
        "price": book.price,
        "price_with_tax": round(price_with_tax, 2)
    }
'''
# dodane Lesson 33 task 10
# ===== Swagger security (żeby pojawiło się pole X-API-Key) =====

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    # 🔐 Upewniamy się, że "components" istnieje
    if "components" not in openapi_schema:
        openapi_schema["components"] = {}

    openapi_schema["components"]["securitySchemes"] = {
        "ApiKeyAuth": {
            "type": "apiKey",
            "in": "header",
            "name": "X-API-Key",
        }
    }

    openapi_schema["security"] = [{"ApiKeyAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi