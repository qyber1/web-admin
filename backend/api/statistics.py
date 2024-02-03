from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse

from .login import get_current_user
from .main import get_template

statistics_router = APIRouter()


@statistics_router.get('/', dependencies=[Depends(get_current_user)], response_class=HTMLResponse)
async def get_statistics(request: Request) -> HTMLResponse:
    return get_template().TemplateResponse("statistics.html", {
        "request": request
    })

