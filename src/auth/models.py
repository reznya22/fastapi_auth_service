from sqlalchemy.sql import expression

from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class UserORM(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(
        default=True,
        server_default=expression.true(),
    )
