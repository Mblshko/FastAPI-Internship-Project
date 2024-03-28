from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base import Base

if TYPE_CHECKING:
    from .users import User


class TimestampModel(Base):
    __abstract__ = True

    created: Mapped[datetime] = mapped_column(default=datetime.now())
    updated: Mapped[datetime] = mapped_column(default=datetime.now())


class Article(TimestampModel):
    __tablename__ = "article"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), unique=True)
    content: Mapped[str] = mapped_column(Text, default="", server_default="")
    is_published: Mapped[bool] = mapped_column(default=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="articles")

    comments: Mapped[list["Comment"]] = relationship(back_populates="article")


class Comment(TimestampModel):
    __tablename__ = "comment"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(255), nullable=False)
    article_id: Mapped[int] = mapped_column(ForeignKey("article.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user: Mapped["User"] = relationship(back_populates="comments")
    article: Mapped["Article"] = relationship(back_populates="comments")
