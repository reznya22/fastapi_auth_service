from fastapi import FastAPI
from src.auth.router import router as auth_router


app = FastAPI(
    title="tumch.",
    docs_url="/api/docs",
    description="Authentication service"
)

app.include_router(auth_router, prefix="/api/v1/users")
