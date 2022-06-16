
from fastapi import APIRouter

from src.controller.api.login import index, login
from src.controller.api.test import read_item

ApiRouter = APIRouter(prefix="/v1", tags=["api路由"])


@ApiRouter.get('/input')
async def home(num: int):
    return {"num": num, "data": [{"num": num, "data": []}, {"num": num, "data": []}]}

ApiRouter.get("/index", tags=["api路由"], summary="注册接口")(index)

ApiRouter.post("/login", tags=["api路由"], summary="登陆接口")(login)

# test
ApiRouter.get("/items/{item_id}", tags=["api路由"], summary="测试接口")(read_item)
