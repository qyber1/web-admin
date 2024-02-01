from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


index_router = APIRouter()
templates = Jinja2Templates(directory='frontend/templates')
TemplateResponse_ = templates.TemplateResponse


@index_router.get('/index')
async def start_page(request: Request) -> TemplateResponse_:
    return templates.TemplateResponse(
        'index.html', {
            'request': request
        }
    )
