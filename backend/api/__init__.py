from fastapi import APIRouter

from .login import auth_router
from .index import index_router
from .employers import employer_router
from .departments import departments_router
from .statistics import statistics_router
from .settings import settings_router

root_router = APIRouter()

root_router.include_router(
    auth_router,
    prefix="/auth",
)
root_router.include_router(
    index_router
)
root_router.include_router(
    employer_router,
    prefix="/employers"
)

root_router.include_router(
    departments_router,
    prefix="/departments"
)

root_router.include_router(
    statistics_router,
    prefix="/statistics"
)

root_router.include_router(
    settings_router,
    prefix="/settings"
)