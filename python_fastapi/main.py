from fastapi import FastAPI
from routers import users, products

app = FastAPI(title="E-commerce API")

# Dołącz routery
app.include_router(users.router)
app.include_router(products.router)

@app.get("/")
async def root():
    return {"message": "Welcome to E-commerce API"}