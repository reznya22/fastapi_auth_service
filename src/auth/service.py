import uuid

from src.auth.schemas import UserRead
from src.auth.utils import AbstractRepository


class UserService:
    def __init__(self, repository: AbstractRepository):
        self.user_repo: AbstractRepository = repository

    async def find_user_by_id(self, user_id: uuid) -> UserRead:
        user = await self.user_repo.find_by_id(id=user_id)
        return UserRead.from_orm(user)

    # async def add_user(self, user: UserCreate):
    #     hashed_password = hashlib.sha256(str.encode(user.password)).hexdigest()
    #     user_orm = UserORM(
    #         email=user.email,
    #         hashed_password=hashed_password,
    #     )
    #     created_user = await self.user_repo.add_one(user_orm)
    #
    #     return created_user
