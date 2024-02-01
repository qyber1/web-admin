from typing import Annotated

from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

auth_router = APIRouter(prefix='/auth')
templates = Jinja2Templates(directory='frontend/templates')
TemplateResponse_ = templates.TemplateResponse


@auth_router.get('/login')
async def get_login_form(request: Request) -> TemplateResponse_:
    return templates.TemplateResponse(
        'login.html',
        {
        'request': request
        }
    )


@auth_router.post('/login')
async def auth(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    if username =='asd' and password == 'asd':
        return RedirectResponse("/index", status_code=303)
