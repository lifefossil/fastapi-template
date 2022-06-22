from fastapi import Request
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse, summary="企业网站首页")
async def index(request: Request):
    return request.app.state.views.TemplateResponse("index.html", context={"request": request})
