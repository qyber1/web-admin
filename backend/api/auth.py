from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

auth_router = APIRouter(prefix='/auth')
templates = Jinja2Templates(directory='frontend/templates')

TemplateResponse_ = templates.TemplateResponse
class User(BaseModel):
    username: str
    password: str


@auth_router.get('/login')
async def get_login_form(request: Request) -> TemplateResponse_:
    return templates.TemplateResponse(
        'login.html',
        {
        'request': request
        }
    )


@auth_router.post('/login')
async def auth(user: User):
    return f'Welcome, {user.username}'
