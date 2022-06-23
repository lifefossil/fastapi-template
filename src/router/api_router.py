from fastapi import APIRouter

from src.controller.api.login import router as login_router
from src.controller.api.login import login
from src.controller.api.retis_test import router as redis_router


api_router = APIRouter(prefix="/api", tags=["api路由"])

# 通过注解引入
api_router.include_router(login_router)
api_router.include_router(redis_router)


# 通过函数模式调用
api_router.post("/login", tags=["api路由"], summary="登陆接口")(login)