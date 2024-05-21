from fastapi import APIRouter

router = APIRouter()


@router.get("/user/")
async def read_user(name: str = "", password: str = ""):
    if not name or not password:
        return {"msg": "ERROR"}
    if name == "fanhang" and password == "123456":
        return {"msg": "ok"}
    else:
        return {"msg": "fail"}
