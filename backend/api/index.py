from fastapi import APIRouter, Request, Depends, HTTPException, Response
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from backend.api.login import get_current_user
from backend.utils.models.models import Admin

index_router = APIRouter()
templates = Jinja2Templates(directory='frontend/templates')
TemplateResponse_ = templates.TemplateResponse


class User(BaseModel):
    username: str
    password: str


@index_router.get('/index')
async def start_page(request: Request, current_user: Admin = Depends(get_current_user)) -> TemplateResponse_:
    return templates.TemplateResponse(
        'index.html', {
            'request': request,
            'current_user': current_user.username
        }
    )
