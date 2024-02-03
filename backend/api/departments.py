from fastapi import APIRouter, Request, Depends

from .login import get_current_user
from .main import TemplateResponse_

departments_router = APIRouter()


@departments_router.get('/', dependencies=[Depends(get_current_user)])
async def get_departments(request: Request) -> TemplateResponse_:
    return TemplateResponse_("departments.html", {
        "request": request
    })

