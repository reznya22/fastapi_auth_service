import uuid

from fastapi_users import FastAPIUsers

from src.auth.models import UserORM
from src.auth.token_config import auth_backend
from src.auth.user_manager import get_user_manager


fastapi_users = FastAPIUsers[UserORM, uuid.UUID](
    get_user_manager,
    [auth_backend],
)


current_user = fastapi_users.current_user()
current_superuser = fastapi_users.current_user(superuser=True)
