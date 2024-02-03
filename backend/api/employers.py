from fastapi import APIRouter, Request, Depends

from .login import get_current_user
from .main import TemplateResponse_

employer_router = APIRouter()


@employer_router.get('/', dependencies=[Depends(get_current_user)])
async def get_employers(request: Request) -> TemplateResponse_:
    return TemplateResponse_("employers.html", {
        "request": request
    })

