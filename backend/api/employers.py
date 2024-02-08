from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession

from .login import get_current_user
from .main import get_template
from ..utils.db.connection import get_session
from ..utils.db.query import _get_all_departments, _get_employers_from_department

employer_router = APIRouter()


@employer_router.get('/', dependencies=[Depends(get_current_user)])
async def get_employers(request: Request, session: AsyncSession = Depends(get_session)) -> HTMLResponse:
    result = await _get_all_departments(session)
    return get_template().TemplateResponse("employers.html", {
        "request": request,
        "departments": result
    })


@employer_router.get('/{item_id}')
async def get_current_department_with_employers(request: Request, item_id: int, session: AsyncSession = Depends(get_session)) -> HTMLResponse:
    employers = await _get_employers_from_department(session, item_id)
    return get_template().TemplateResponse("employer_current_department.html", {
        "request": request,
        "full_info": employers
    })
