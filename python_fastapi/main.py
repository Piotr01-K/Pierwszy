from fastapi import FastAPI, Request, Path
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import time
import logging
from fastapi.security import APIKeyHeader
from fastapi import Security
import asyncio
from datetime import datetime   # dodane Lesson 33 task 1
import random # dodane Lesson 33 task 1

API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name="X-API-Key")

app = FastAPI()

class AppState:
    db_connection = None
    cache = {}
    background_worker_task = None

app.state = AppState()


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
@app.middleware("http")
async def verify_api_key(request: Request, call_next):
     # pozwalamy Swaggerowi działać bez klucza
    if request.url.path in ["/docs", "/openapi.json", "/redoc"]:
        return await call_next(request)

    api_key = request.headers.get(API_KEY_NAME)

    if api_key != "secret-key-123":
        from fastapi.responses import JSONResponse
        return JSONResponse(
            status_code=401,
            content={"detail": "Invalid or missing API Key"},
        )

    return await call_next(request)


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

# dodane Lesson 33 task 1
@app.get("/")
async def root():
    return {"message": "Hello"}

@app.get("/time")
async def get_time():
    return {"time": datetime.now()}

@app.get("/random")
async def get_random_number():
    return {"number": random.randint(1, 100)}

# dodane Lesson 33 task 2
@app.get("/greet/{name}")
async def greet_user(
    name: str = Path(min_length=2)
):
    return {"message": f"Hello {name}"}