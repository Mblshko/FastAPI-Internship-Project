from datetime import datetime
from typing import TYPE_CHECKING

from fastapi import Depends
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base import Base, get_db

if TYPE_CHECKING:
    from .articles import Article, Comment


class User(Base, SQLAlchemyBaseUserTable[int]):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(default=datetime.now())
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    comments: Mapped[list["Comment"]] = relationship(back_populates="user")
    articles: Mapped[list["Article"]] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(uselist=False, back_populates="user")


async def get_user_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyUserDatabase(session, User)


class Profile(Base):
    __tablename__ = "profile"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), unique=True)

    user: Mapped["User"] = relationship(back_populates="profile")
