from src.controller.api.base import ApiRouter
from src.controller.views.base import ViewsRouter
from fastapi import APIRouter


AllRouter = APIRouter()
# 视图路由
AllRouter.include_router(ViewsRouter)
# API路由
AllRouter.include_router(ApiRouter)