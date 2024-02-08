from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from .login import get_current_user
from .main import get_template

from backend.utils.db.connection import get_session
from backend.utils.db.query import _get_all_departments, _insert_new_department

departments_router = APIRouter()


@departments_router.get('/', dependencies=[Depends(get_current_user)], response_class=HTMLResponse)
async def get_departments(request: Request,
                          session: AsyncSession = Depends(get_session)) -> HTMLResponse:
    result = await _get_all_departments(session)
    print(result)
    return get_template().TemplateResponse("departments.html", {
        "request": request,
        "departments": result
    })


@departments_router.get('/add', dependencies=[Depends(get_current_user)], response_class=HTMLResponse)
async def add_new_departments_view(request: Request) -> HTMLResponse:
    return get_template().TemplateResponse("add_departments.html", {
        "request": request
    })


@departments_router.post('/add', dependencies=[Depends(get_current_user)], response_class=HTMLResponse)
async def add_new_departments(title: str = Form(),
                              session: AsyncSession = Depends((get_session))) -> HTMLResponse:
    await _insert_new_department(session, title)
    return RedirectResponse('/departments/', status_code=303)