from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from .login import get_current_user
from .main import get_template

settings_router = APIRouter()


@settings_router.get('/', dependencies=[Depends(get_current_user)], response_class=HTMLResponse)
async def get_settings(request: Request) -> HTMLResponse:
    return get_template().TemplateResponse("settings.html", {
        "request": request
    })

