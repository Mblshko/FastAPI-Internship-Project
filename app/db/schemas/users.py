from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    username: str
    password: str


class User(UserBase):
    id: int
    created: str

    class Config:
        orm_mode = True
