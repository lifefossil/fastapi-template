from src.router.api_router import api_router
from src.router.views_router import view_router
from fastapi import APIRouter


AllRouter = APIRouter()
# 视图路由
AllRouter.include_router(view_router)
# API路由
AllRouter.include_router(api_router)