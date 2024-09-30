import asyncio
import datetime

from pydantic import BaseModel
from fastapi import APIRouter, status

post_router = APIRouter()


class Posts(BaseModel):
    id: int
    title: str
    content: str
    created_at: str


posts = [
    Posts(
        id=1,
        title="Post 1",
        content="This is the content of post 1",
        created_at="2021-06-15 12:00:00",
    ),
    Posts(
        id=2,
        title="Post 2",
        content="This is the content of post 2",
        created_at="2021-06-16 12:00:00",
    ),
    Posts(
        id=3,
        title="Post 3",
        content="This is the content of post 3",
        created_at="2021-06-17 12:00:00",
    ),
]


@post_router.get("/posts", status_code=status.HTTP_200_OK)
async def get_posts():
    await asyncio.sleep(10)
    print(datetime.datetime.now())
    return posts


@post_router.get("/posts/{id}", status_code=status.HTTP_200_OK)
async def get_post_by_id(id: int):
    await asyncio.sleep(10)
    print(datetime.datetime.now())
    return [post for post in posts if post.id == id]


@post_router.post("/posts")
async def create_post(post: Posts):
    posts.append(post)
