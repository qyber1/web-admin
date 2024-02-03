from fastapi import APIRouter, Request, Depends

from .login import get_current_user
from .main import TemplateResponse_

settings_router = APIRouter()


@settings_router.get('/', dependencies=[Depends(get_current_user)])
async def get_settings(request: Request) -> TemplateResponse_:
    return TemplateResponse_("settings.html", {
        "request": request
    })

