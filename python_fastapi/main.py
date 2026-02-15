from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

# Path parameter - część ścieżki URL
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """
    Pobiera użytkownika po ID.
    FastAPI automatycznie waliduje, czy user_id to int.
    """
    return {"user_id": user_id, "name": f"User {user_id}"}


# Query parameters - parametry po znaku ?
@app.get("/search")
async def search_items(
    query: str,  # Wymagany parametr
    limit: int = 10,  # Opcjonalny z wartością domyślną
    offset: int = 0
):
    """
    Wyszukuje przedmioty z paginacją.
    """
    return {
        "query": query,
        "limit": limit,
        "offset": offset,
        "results": [f"Item {i}" for i in range(offset, offset + limit)]
    }


# Zaawansowane query parameters z walidacją
@app.get("/items")
async def get_items(
    skip: int = 0,
    limit: int = Query(default=10, ge=1, le=100),
    search: Optional[str] = Query(None, min_length=3, max_length=50)
):
    """
    Pobiera przedmioty z zaawansowaną walidacją.
    """
    result = {"skip": skip, "limit": limit}
    if search:
        result["search"] = search
    return result