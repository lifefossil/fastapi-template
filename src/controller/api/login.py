from typing import List
from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()


class Login(BaseModel):
    username: str
    password: str
    user: List[int]


@router.get('/index', summary="")
def index(age: int = 80):
    return {"fun": "/index", "age": age}


def login(data: Login):
    return data