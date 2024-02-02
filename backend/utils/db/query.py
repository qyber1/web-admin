from sqlalchemy.ext.asyncio import AsyncSession

from backend.utils.db.models import UserAdmin
from sqlalchemy import select


async def _get_current_user(session: AsyncSession, username: str):
    result = await session.execute(
            select(UserAdmin.username, UserAdmin.password).where(UserAdmin.username == username))
    result = result.fetchone()
    return result