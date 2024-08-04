from typing import Sequence, Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.schemas import UserOutSchema
from src.database import get_db
from src.auth.models import UserORM
from src.auth.utils import AbstractRepository


class UserRepository(AbstractRepository):
    def __init__(self, db: Annotated[AsyncSession, Depends(get_db)]):
        self.db = db

    async def find_all(self) -> Sequence[UserOutSchema]:
        query = select(UserORM)
        result = await self.db.scalars(query)
        return [UserOutSchema.from_orm(user) for user in result.all()]

    async def add_one(self, user_orm: UserORM) -> UserOutSchema:
        self.db.add(user_orm)
        await self.db.flush()
        await self.db.commit()
        return UserOutSchema.from_orm(user_orm)
