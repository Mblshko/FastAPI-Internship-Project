from pydantic import BaseModel, ConfigDict


class CommentBase(BaseModel):
    text: str


class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):
    """Response"""

    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    article_id: int
