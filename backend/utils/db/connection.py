from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import get_config


DATABASE_URL = get_config()
TEST_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/solo_db_test"
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

Base = declarative_base()


async def get_session() -> AsyncSession:
    async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session, session.begin():
        yield session