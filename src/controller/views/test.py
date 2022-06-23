from fastapi import Request
from fastapi import APIRouter
from fastapi import Form
from fastapi.responses import HTMLResponse
from src.model.admin import User

router = APIRouter()


@router.get('/test/register', response_class=HTMLResponse)
async def reg(req: Request):
    return req.app.state.views.TemplateResponse('register.html', {'request': req})

@router.post('/test/result', response_class=HTMLResponse)
async def reg(req: Request, username: str = Form(...), password: str = Form(...)):
    add_user = await User().create(username=username, password=password)
    print("插入的自增ID2", add_user.pk)
    print("插入的用户名", add_user.username)
    return req.app.state.views.TemplateResponse('result.html', {'request': req,
                                                                'username': username,
                                                                'password': password})