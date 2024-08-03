from typing import Annotated

from fastapi import APIRouter, Depends

from src.auth.schemas import UserInSchema, UserOutSchema
from src.auth.service import UserService
from src.auth.dependencies import user_service_dep

router = APIRouter(tags=["Users"])


@router.get("/", response_model=list[UserOutSchema])
async def get_all_users(
        user_service: Annotated[UserService, Depends(user_service_dep)]
) -> list[UserOutSchema]:

    users = await user_service.find_users()
    return users


@router.post("/", response_model=UserOutSchema)
async def create_user(
        user: UserInSchema,
        user_service: Annotated[UserService, Depends(user_service_dep)]
) -> UserOutSchema:

    created_user = await user_service.add_user(user)
    return UserOutSchema.from_orm(created_user)
