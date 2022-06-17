from fastapi import APIRouter
from src.controller.views.biz import router as biz_router

view_router = APIRouter(tags=["view router"])

view_router.include_router(biz_router)

