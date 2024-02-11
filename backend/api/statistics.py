from datetime import timedelta

from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession

from .login import get_current_user
from .main import get_template
from ..utils.db.connection import get_session

from ..utils.db.query import _get_employer_statistics
statistics_router = APIRouter()


async def total_time(time_: timedelta):
    total_seconds = time_.total_seconds()

    hours, remainder = divmod(int(total_seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{:02}:{:02}:{:02}".format(hours, minutes, seconds)


async def time_formatted(data: list):
    result = []

    for item in data:
        result.append({
            "name": item[0],
            "start": item[1].strftime("%H:%M:%S"),
            "end": item[2].strftime("%H:%M:%S") if item[2] else ' git ',
            "total": await total_time(item[3]) if item[3] else ' ',
            "date": item[4],
            "comment": item[5] if item[5] else ' '
        })

    return result



@statistics_router.get('/', dependencies=[Depends(get_current_user)], response_class=HTMLResponse)
async def get_statistics(request: Request) -> HTMLResponse:
    return get_template().TemplateResponse("statistics.html", {
        "request": request,
    })

@statistics_router.get('/{user_id}', dependencies=[Depends(get_current_user)], response_class=HTMLResponse)
async def get_statistics_current_employer(user_id: int, request: Request, session: AsyncSession = Depends(get_session)) -> HTMLResponse:
    stat = await _get_employer_statistics(session, user_id)
    data = await time_formatted(stat)
    return get_template().TemplateResponse("statistics.html", {
        "request": request,
        "statistic": data
    })

