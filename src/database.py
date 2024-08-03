from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.config import settings
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(
    url=settings.DATABSE_URL,
    echo=True
)

session_factory = async_sessionmaker(
    engine,
    expire_on_commit=False,
    autoflush=False
)


async def get_db() -> AsyncGenerator:
    async with session_factory() as session:
        yield session


class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention=settings.naming_conventions
    )
