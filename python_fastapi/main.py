from fastapi import FastAPI
app = FastAPI(
    title="Moja Pierwsza API",
    description="API do zarządzania użytkownikami i produktami",
    version="1.0.0"
)

@app.get("/users", tags=["Users"])
async def get_users():
    """
    Pobiera listę wszystkich użytkowników.
    """
    return [
        {"id": 1, "name": "Jan Kowalski"},
        {"id": 2, "name": "Anna Nowak"}
    ]

@app.get("/products", tags=["Products"])
async def get_products():
    """
    Pobiera listę produktów.
    """
    return [
        {"id": 1, "name": "Laptop", "price": 3000},
        {"id": 2, "name": "Mouse", "price": 50}
    ]