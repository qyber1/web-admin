from fastapi import APIRouter, Request, Depends

from .login import get_current_user
from .main import TemplateResponse_

statistics_router = APIRouter()


@statistics_router.get('/', dependencies=[Depends(get_current_user)])
async def get_statistics(request: Request) -> TemplateResponse_:
    return TemplateResponse_("statistics.html", {
        "request": request
    })

