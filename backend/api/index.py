from fastapi import APIRouter, Request, Depends
from pydantic import BaseModel

from backend.api.login import get_current_user
from backend.utils.models.models import Admin
from .main import TemplateResponse_

index_router = APIRouter()


class User(BaseModel):
    username: str
    password: str


@index_router.get('/')
@index_router.get('/index')
async def start_page(request: Request, current_user: Admin = Depends(get_current_user)) -> TemplateResponse_:
    return TemplateResponse_(
        'index.html', {
            'request': request,
            'current_user': current_user.username
        }
    )
