from sqlalchemy.ext.asyncio import AsyncSession

from backend.utils.db.models import UserAdmin, Department
from sqlalchemy import select


async def _get_current_user(session: AsyncSession, username: str) -> tuple[str, str]:
    result = await session.execute(
            select(UserAdmin.username, UserAdmin.password).where(UserAdmin.username == username))
    return result.fetchone()


async def _get_all_departments(session: AsyncSession) -> list[tuple[str,]]:
    result = await session.execute(
        select(Department.title)
    )
    return result.fetchall()
