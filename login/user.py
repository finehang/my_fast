import datetime
from typing import Union, Annotated
from uuid import UUID

from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel, Field, HttpUrl

router = APIRouter()


class User(BaseModel):
    user_name: str
    pass_word: str
    gender: str = "男"
    age: int


@router.get("/user/")
async def read_user(name: str = "", password: str = ""):
    if not name or not password:
        return {"msg": "ERROR"}
    if name == "fanhang" and password == "123456":
        return {"msg": "ok"}
    else:
        return {"msg": "fail"}


@router.post("/user/")
async def create_user(user: User):
    return {"msg": "ok", "user": user.dict()}


@router.get("/items/")
# 使用 Query 为查询参数声明更多的校验和元数据的方式相同
# 设置别名 q-->item-query
async def read_items(
        q: Union[str, None] = Query(
            default=None,
            alias="item-query",
            title="Query string Okkkkk",
            description="Query string for the items to search in the database that have a good match",
            deprecated=True)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@router.get("/items/{item_id}")
async def read_items(
        *,
        item_id: int = Path(title="The ID of the item to get", ge=1),
        size: float = Query(gt=0, lt=10.5),
        q: str
):
    # 使用Path为查询参数声明更多的校验和元数据的方式相同
    # 将*之后的所有参数都应作为关键字参数(键值对), 也被称为kwargs, 来调用, 即使它们没有默认值
    # 使用*将允许非默认形参出现在默认形参之后
    results = {"item_id": item_id}
    if q:
        results.update({"q": q, "size": size})
    return results


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


class Member(BaseModel):
    username: str
    full_name: str | None = None


@router.put("/items0/{item_id}")
async def update_item(
        item_id: int, item: Item, user: Member, importance: Annotated[int, Body()]
):
    """
    使用Body为查询参数声明更多的校验和元数据的方式相同
    多个模型
    存在两个以上模型的话, 会自动进行嵌套
    {
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
    }
    只有一个不会嵌套, 但可以使用, item: Annotated[Item, Body(embed=True)]强行将其嵌套
    {
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
    }
    :param item_id:
    :param item:
    :param user:
    :param importance:
    :return:
    """
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


# 使用 Pydantic 的 Field 在 Pydantic 模型内部声明校验和元数据。

class Product(BaseModel):
    name: str
    description: str | None = Field(
        default=None,
        alias="product-desc",
        title="Query string Okkkkkk",
        description="Query string for the products to search in the database that have a good match",
    )
    price: float = Field(
        gt=0.00,
        lt=100.00,
        alias="product-price",
        title="The price of the product",
        description="The price of the product",
        examples=[3.2],
    )


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Product, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results


# 使用模型属性嵌套和模型嵌套, 模型的属性类型是列表, 或者是其他模型


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item1(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []
    image: Image | None = None


@router.put("/item1/{item_id}")
async def update_item(item_id: int, item: Item1):
    """
    {
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": ["rock", "metal", "bar"],
    "image": {
        "url": "https://example.com/baz.jpg",
        "name": "The Foo live"
        }
    }
    :param item_id:
    :param item:
    :return:
    """
    results = {"item_id": item_id, "item": item}
    return results


@router.put("/items2/{item_id}")
async def read_items(
        item_id: UUID,
        start_datetime: Annotated[datetime.datetime, Body()],
        end_datetime: Annotated[datetime.datetime, Body()],
        process_after: Annotated[datetime.timedelta, Body()],
        repeat_at: Annotated[datetime.time | None, Body()] = None,
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }
