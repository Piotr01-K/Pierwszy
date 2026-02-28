import strawberry
from typing import List, Optional
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView

# ================================
#   TYPY GRAPHQL
# ================================

@strawberry.type
class User:
    id: int
    name: str
    email: str

    # relacja: User → Posts
    @strawberry.field
    def posts(self) -> List["Post"]:
        return [
            post for post in fake_posts_db
            if post.author_id == self.id
        ]


@strawberry.type
class Post:
    id: int
    title: str
    content: str
    author_id: int

    # relacja: Post → Author
    @strawberry.field
    def author(self) -> Optional[User]:
        for user in fake_users_db:
            if user.id == self.author_id:
                return user
        return None


# ================================
#   FAKE BAZA DANYCH
# ================================

fake_users_db = [
    User(id=1, name="Jan Kowalski", email="jan@example.com"),
    User(id=2, name="Anna Nowak", email="anna@example.com"),
]

fake_posts_db = [
    Post(id=1, title="Python jest super", content="...", author_id=1),
    Post(id=2, title="GraphQL tutorial", content="...", author_id=1),
    Post(id=3, title="Asyncio w praktyce", content="...", author_id=2),
]


# ================================
#   QUERY
# ================================

@strawberry.type
class Query:

    @strawberry.field
    def users(self) -> List[User]:
        return fake_users_db

    @strawberry.field
    def user(self, id: int) -> Optional[User]:
        for u in fake_users_db:
            if u.id == id:
                return u
        return None

    @strawberry.field
    def posts(self, authorId: Optional[int] = None) -> List[Post]:
        if authorId is None:
            return fake_posts_db

        return [
            post for post in fake_posts_db
            if post.author_id == authorId
        ]

    @strawberry.field
    def searchUsers(self, name: str) -> List[User]:
        name_lower = name.lower()

        return [
            user for user in fake_users_db
            if name_lower in user.name.lower()
        ]


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