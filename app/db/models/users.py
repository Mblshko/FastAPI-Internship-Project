from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    created = Column(DateTime, default=datetime.now())
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    comments = relationship("Comment", uselist=False, back_populates="user")
    profile = relationship("Profile", uselist=False, back_populates="user")


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="profile")
