from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import UserORM
from src.database import get_db

from src.auth.repository import UserRepository
from src.auth.service import UserService


async def user_service_dep(db: AsyncSession = Depends(get_db)):
    yield UserService(UserRepository(db=db))


async def get_user_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyUserDatabase(session, UserORM)
