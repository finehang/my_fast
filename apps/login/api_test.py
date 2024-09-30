from typing import Optional

from fastapi import APIRouter, Form, Header

router = APIRouter()


@router.get("/")
async def root():
    print("hello")
    return {"message": "Hello World"}


# 路径参数
@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# 查询参数
@router.get("/main/")
async def main(name: str, age: int, home: str = "henan"):
    return {"message": f"Hello {name}, {age}, {home}"}


# 获取请求标头
@router.get("/header/")
async def header(
    host: Optional[str] = Header(None), accept_language: Optional[str] = Header(None)
):
    request_headers = {"Host": host, "Accept-Language": accept_language}
    return {"message": f"Hello {host} {accept_language}, {request_headers}"}


# 获取表单参数
@router.post("/form/")
async def form(
    name: str = Form(...),
    sex: str = Form(...),
    age: int = Form(...),
    home: str = Form(...),
):
    return {"name": name, "sex": sex, "age": age, "home": home}
