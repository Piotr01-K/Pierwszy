import strawberry
from typing import Optional, List
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView

# ========================================
# 🗄️ FAKE BAZA
# ========================================

fake_users_db = [
    {"id": 1, "name": "Jan Kowalski", "email": "jan@example.com"},
    {"id": 2, "name": "Anna Nowak", "email": "anna@example.com"},
    {"id": 3, "name": "Piotr Wiśniewski", "email": "piotr@example.com"},
]

# ========================================
# 🧩 Typ GraphQL
# ========================================

@strawberry.type
class User:
    id: int
    name: str
    email: str

# ========================================
# 🔍 Query
# ========================================

@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int) -> Optional[User]:
        """Zwraca użytkownika po ID"""
        for u in fake_users_db:
            if u["id"] == id:
                return User(**u)
        return None

# ========================================
# 🚀 Schema + app
# ========================================

schema = strawberry.Schema(query=Query)

app = web.Application()

app.router.add_route(
    "*",
    "/graphql",
    GraphQLView(schema=schema),
)

# ========================================
# ▶️ RUN
# ========================================

if __name__ == "__main__":
    print("🚀 GraphQL działa na http://localhost:8000/graphql")
    web.run_app(app, host="localhost", port=8000)