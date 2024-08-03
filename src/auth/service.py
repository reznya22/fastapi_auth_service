import hashlib

from src.auth.models import UserORM
from src.auth.schemas import UserInSchema, UserOutSchema
from src.auth.utils import AbstractRepository


class UserService:
    def __init__(self, repository: AbstractRepository):
        self.user_repo: AbstractRepository = repository

    async def add_user(self, user: UserInSchema):
        hashed_password = hashlib.sha256(str.encode(user.password)).hexdigest()
        user_orm = UserORM(
            username=user.username,
            email=user.email,
            password=hashed_password
        )
        created_user = await self.user_repo.add_one(user_orm)

        return created_user

    async def find_users(self) -> list[UserOutSchema]:
        users = await self.user_repo.find_all()
        return [UserOutSchema.from_orm(user) for user in users]
