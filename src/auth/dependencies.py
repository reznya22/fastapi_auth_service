from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.auth.repository import UserRepository
from src.auth.service import UserService


def user_service_dep(db: AsyncSession = Depends(get_db)):
    return UserService(UserRepository(db=db))
