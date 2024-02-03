from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from .login import get_current_user
from .main import get_template

employer_router = APIRouter()


@employer_router.get('/', dependencies=[Depends(get_current_user)])
async def get_employers(request: Request) -> HTMLResponse:
    return get_template().TemplateResponse("employers.html", {
        "request": request
    })

