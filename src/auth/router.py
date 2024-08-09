from typing import Annotated

from fastapi import APIRouter, Depends

from src.auth.fastapi_users_router import current_user
from src.auth.models import UserORM
from src.auth.schemas import UserRead

router = APIRouter(tags=["users"])


@router.get("/me/", response_model=UserRead)
async def get_current_user(
    user: Annotated[UserORM, Depends(current_user)],  # fmt: skip
) -> UserRead:
    return UserRead.from_orm(user)


#
# @router.get("/", response_model=list[UserOutSchema])
# async def get_all_users(
#     user_service: Annotated[UserService, Depends(user_service_dep)]
# ) -> Sequence[UserOutSchema]:
#
#     users = await user_service.find_users()
#     return users
#
#
# @router.post("/", response_model=UserOutSchema)
# async def create_user(
#     user: UserInSchema,
#     user_service: Annotated[UserService, Depends(user_service_dep)],
# ) -> UserOutSchema:
#
#     created_user = await user_service.add_user(user)
#     return created_user
