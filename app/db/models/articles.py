from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class TimestampModel(Base):
    __abstract__ = True

    created = Column(DateTime, default=datetime.now())
    updated = Column(DateTime, default=datetime.now())


class Article(TimestampModel):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True)
    content = Column(String(1000))
    is_published = Column(Boolean, default=True)

    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="articles")

    comments = relationship("Comment", back_populates="article")


class Comment(TimestampModel):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    text = Column(String(255))
    article_id = Column(Integer, ForeignKey("articles.id"))
    author_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates="comment")
    article = relationship("Article", back_populates="comment")
