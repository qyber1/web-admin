from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from backend.api.login import get_current_user
from backend.utils.models.models import Admin
from .main import get_template

index_router = APIRouter()


class User(BaseModel):
    username: str
    password: str


@index_router.get('/', response_class=HTMLResponse)
@index_router.get('/index', response_class=HTMLResponse)
async def start_page(request: Request, current_user: Admin = Depends(get_current_user)) -> HTMLResponse:
    return get_template().TemplateResponse(
        'index.html', {
            'request': request,
            'current_user': current_user.username
        }
    )
