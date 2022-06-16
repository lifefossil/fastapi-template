from fastapi import APIRouter
from starlette.responses import HTMLResponse

from src.controller.views.home import home

ViewsRouter = APIRouter()


ViewsRouter.get("/items/{id}", response_class=HTMLResponse)(home)