from pydantic import BaseModel, ConfigDict


class CommentBase(BaseModel):
    text: str


class CommentCreate(CommentBase):
    pass


class CommentRead(CommentBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: str
    article_id: str
