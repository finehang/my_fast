from fastapi import FastAPI

from apps.login import user, api_test, posts

app = FastAPI()

app.include_router(user.router, prefix="/v1")
app.include_router(api_test.router, prefix="/v0")
app.include_router(posts.post_router, prefix="/v0")
