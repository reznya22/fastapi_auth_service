import uuid
from typing import Sequence, Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.schemas import UserRead

from src.database import get_db
from src.auth.models import UserORM
from src.auth.utils import AbstractRepository


class UserRepository(AbstractRepository):
    def __init__(self, db: Annotated[AsyncSession, Depends(get_db)]):
        self.db = db

    async def find_by_id(self, user_id: uuid) -> UserRead:
        stmt = select(UserORM).where(UserORM.id == id)
        user = await self.db.scalars(stmt)
        return UserRead.from_orm(user)


#     async def add_one(self, user_orm: UserORM) -> UserOutSchema:
#         self.db.add(user_orm)
#         await self.db.flush()
#         await self.db.commit()
#         return UserOutSchema.from_orm(user_orm)
