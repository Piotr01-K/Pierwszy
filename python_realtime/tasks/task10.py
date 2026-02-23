import strawberry
from typing import List, Optional
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView

# ================================
#   FAKE BAZA DANYCH
# ================================

fake_users_db = [
    {"id": 1, "name": "Jan Kowalski", "email": "jan@example.com"},
    {"id": 2, "name": "Anna Nowak", "email": "anna@example.com"},
]

fake_posts_db = [
    {"id": 1, "title": "Python jest super", "content": "...", "author_id": 1},
    {"id": 2, "title": "GraphQL tutorial", "content": "...", "author_id": 1},
    {"id": 3, "title": "Asyncio w praktyce", "content": "...", "author_id": 2},
]

# ================================
#   TYPY GRAPHQL
# ================================

@strawberry.type
class Post:
    id: int
    title: str
    content: str
    author_id: int

    #   relacja: Post → Author
    @strawberry.field
    def author(self) -> Optional["User"]:
        for user in fake_users_db:
            if user["id"] == self.author_id:
                return User(**user)
        return None


@strawberry.type
class User:
    id: int
    name: str
    email: str

    #   relacja: User → Posts
    @strawberry.field
    def posts(self) -> List[Post]:
        user_posts = [
            Post(**post)
            for post in fake_posts_db
            if post["author_id"] == self.id
        ]
        return user_posts


# ================================
#   QUERY
# ================================

@strawberry.type
class Query:

    @strawberry.field
    def users(self) -> List[User]:
        return [User(**u) for u in fake_users_db]

    @strawberry.field
    def user(self, id: int) -> Optional[User]:
        for u in fake_users_db:
            if u["id"] == id:
                return User(**u)
        return None

    @strawberry.field
    def posts(self) -> List[Post]:
        return [Post(**p) for p in fake_posts_db]


# ================================
#   SCHEMA + APP
# ================================

schema = strawberry.Schema(query=Query)

app = web.Application()
app.router.add_route(
    "*",
    "/graphql",
    GraphQLView(schema=schema, graphql_ide="graphiql"),
)

# ================================
#   RUN
# ================================

if __name__ == "__main__":
    print("🚀 GraphQL server działa na http://localhost:8000/graphql")
    web.run_app(app, host="localhost", port=8000)