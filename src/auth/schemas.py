import uuid
from pydantic import BaseModel, EmailStr
from fastapi_users import schemas, models


class UserRead(schemas.BaseUser[uuid.UUID]):
    id: models.ID
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False

    @classmethod
    def from_orm(cls, orm_obj):
        return UserRead(
            id=orm_obj.id,
            email=orm_obj.email,
            is_superuser=orm_obj.is_superuser,
            is_active=orm_obj.is_active,
            is_verified=orm_obj.is_verified,
        )


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str
    is_active: bool | None = True
    is_superuser: bool | None = False


# class UserInSchema(BaseModel):
#     username: str
#     email: str
#     password: str
#
#
# class UserOutSchema(BaseModel):
#     id: int
#     username: str
#     email: str
#
#     @classmethod
#     def from_orm(cls, orm_obj):
#         return UserOutSchema(
#             id=orm_obj.id, username=orm_obj.username, email=orm_obj.email
#         )

# class UserUpdate(schemas.BaseUserUpdate):
#     pass
