from pydantic import BaseModel


class UserInSchema(BaseModel):
    username: str
    email: str
    password: str


class UserOutSchema(BaseModel):
    id: int
    username: str
    email: str

    @classmethod
    def from_orm(cls, orm_obj):
        return UserOutSchema(
            id=orm_obj.id,
            username=orm_obj.username,
            email=orm_obj.email
        )
