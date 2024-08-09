from fastapi import FastAPI
from src.auth.fastapi_users_router import fastapi_users

from src.auth.router import router as user_router
from src.auth.schemas import UserRead, UserCreate
from src.auth.token_config import auth_backend

app = FastAPI(
    title="tumch.",
    docs_url="/api/docs",
    description="Authentication service",
)

# /login /logout
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/api/auth/jwt",
    tags=["auth"],
)

# /register
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/api/auth",
    tags=["auth"],
)

# /me
app.include_router(
    user_router,
    prefix="/api/users",
)
