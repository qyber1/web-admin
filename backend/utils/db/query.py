from sqlalchemy.ext.asyncio import AsyncSession

from backend.utils.db.models import UserAdmin, Department, User, Worklog
from sqlalchemy import select


async def _get_current_user(session: AsyncSession, username: str) -> tuple[str, str]:
    result = await session.execute(
            select(UserAdmin.username, UserAdmin.password).where(UserAdmin.username == username))
    return result.fetchone()


async def _get_all_departments(session: AsyncSession) -> list[tuple[str,]]:
    result = await session.execute(
        select(Department.title, Department.id)
    )
    return result.fetchall()


async def _insert_new_department(session: AsyncSession, title: str) -> None:
    department = Department(title=title)
    session.add(department)
    await session.commit()
    return


async def _get_employers_from_department(session: AsyncSession, id: int):
    employers = await session.execute(
        select(User.id, User.username, User.job_title, Department.title).join(Department).where(Department.id == id)
    )
    return employers.fetchall()


async def _get_employer_statistics(session: AsyncSession, id: int):
    statistics = await session.execute(
        select(User.username,
               Worklog.start_time,
        Worklog.end_time,
        (Worklog.end_time - Worklog.start_time),
        Worklog.date,
        Worklog.comment).join(User).where(Worklog.user_id == id)
    )

    return statistics.fetchall()